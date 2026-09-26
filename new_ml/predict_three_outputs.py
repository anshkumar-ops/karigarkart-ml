"""Return an object polygon, handicraft type, and material for each joint-class prediction."""
import argparse,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
(ROOT/'tools/config').mkdir(parents=True,exist_ok=True)
os.environ['YOLO_CONFIG_DIR']=str(ROOT/'tools/config')
sys.path.insert(0,str(ROOT/'scripts'))
from common_taxonomy import describe_type

def object_output(info, confidence, polygon, xyxy, width, height, object_id):
    """Image geometry is normalized or in pixels, never real-world size."""
    polygon=[[float(x),float(y)] for x,y in polygon]
    area=abs(sum(polygon[i][0]*polygon[(i+1)%len(polygon)][1]-polygon[(i+1)%len(polygon)][0]*polygon[i][1] for i in range(len(polygon))))/2 if len(polygon)>=3 else 0.0
    bounds=[float(v) for v in xyxy]
    return {'object_id':object_id,'class_name':info['class_name'],
        'handicraft_type':info['handicraft_type'],'material':info['material'],
        **describe_type(info['handicraft_type']),
        'joint_confidence':float(confidence),
        'object_mask_polygon_normalized':polygon,
        'bounding_box_xyxy_pixels':bounds,
        'bounding_box_xyxy_normalized':[v/scale for v,scale in zip(bounds,[width,height,width,height])],
        'visible_mask_area_fraction':area,
        'material_status':'unknown' if info['material']=='unknown' else 'visual_estimate_not_authenticated'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--model',required=True); p.add_argument('--source',required=True)
    p.add_argument('--output',default=str(ROOT/'prediction.json')); p.add_argument('--conf',type=float,default=.4)
    args=p.parse_args()
    from ultralytics import YOLO
    metadata=json.loads((ROOT/'class_metadata.json').read_text()); by_name={m['class_name']:m for m in metadata.values()}
    model=YOLO(args.model)
    expected={int(k):v['class_name'] for k,v in metadata.items()}
    if model.names!=expected: raise ValueError('This checkpoint does not match this dataset taxonomy. Use the NEW multiclass trained best.pt, not the old single-class checkpoint.')
    results=[]
    for prediction in model.predict(args.source,conf=args.conf,verbose=False):
        objects=[]; height,width=prediction.orig_shape
        if prediction.masks is not None:
            for box,polygon in zip(prediction.boxes,prediction.masks.xyn):
                name=prediction.names[int(box.cls.item())]; info=by_name[name]
                objects.append(object_output(info,box.conf.item(),polygon.tolist(),box.xyxy[0].tolist(),width,height,len(objects)+1))
        results.append({'image':prediction.path,'image_width_px':width,'image_height_px':height,
                        'detected_object_count':len(objects),'objects':objects})
    Path(args.output).write_text(json.dumps(results,indent=2),encoding='utf-8'); print(json.dumps(results,indent=2))

if __name__=='__main__': main()
