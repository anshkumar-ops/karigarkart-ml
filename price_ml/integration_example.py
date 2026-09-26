"""Bridge one object from predict_three_outputs.py JSON into the separate price model."""
import argparse,json
from pathlib import Path
from predict import predict_product
def main():
 p=argparse.ArgumentParser();p.add_argument('--yolo-result',type=Path,required=True);p.add_argument('--image-index',type=int,default=0)
 p.add_argument('--object-index',type=int);p.add_argument('--product-form',default='unspecified');a=p.parse_args()
 frames=json.loads(a.yolo_result.read_text(encoding='utf-8'));objects=frames[a.image_index]['objects']
 if not objects:raise ValueError('No object detected; ask the seller to identify the product')
 if a.object_index is None and len(objects)!=1:raise ValueError('Multiple objects: explicitly choose --object-index; do not price the photo as a bundle')
 obj=objects[0 if a.object_index is None else a.object_index]
 if 'joint_confidence' not in obj:raise ValueError('Expected YOLO joint_confidence field')
 print(json.dumps(predict_product({**obj,'product_form':a.product_form}),indent=2))
if __name__=='__main__':main()
