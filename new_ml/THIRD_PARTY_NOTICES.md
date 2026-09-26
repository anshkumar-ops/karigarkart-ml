# Source and annotation-tool notices

- Original YOLO checkpoint: supplied by the user; its embedded metadata identifies Ultralytics and AGPL-3.0. See https://ultralytics.com/license . Copied only for training initialization; it is not the new multiclass trained model.
- Original Roboflow data: the per-source README/YAML attribution files are preserved under `provenance/original_dataset`. `Clay Pot` source metadata states CC BY 4.0. Other sources retain their own notices.
- Product photographs and CSV descriptions: supplied in `Handicraft_products`. No complete redistribution license was found alongside these files; product text references iTokri. The original creators' rights remain applicable. Automatically generated annotations do not grant rights to the photographs.
- Other ZIP notices: copied into their source-named folders in `provenance` where supplied. Missing licenses are not assumed to be public domain.
- SAM 2.1: Meta model, downloaded from Ultralytics assets for local pseudo-mask generation. https://github.com/facebookresearch/sam2 and https://github.com/ultralytics/assets/releases/tag/v8.3.0 . SAM model licensing and Ultralytics implementation licensing remain applicable.
- U2-Net: saliency model from the rembg model release. https://github.com/xuebinqin/U-2-Net and https://github.com/danielgatis/rembg . The ONNX model is used locally for annotation and is not part of the compact training ZIP.
- Annotation-method references: https://docs.ultralytics.com/datasets/segment/ , https://docs.ultralytics.com/models/sam-2/ , https://github.com/danielgatis/rembg/blob/main/rembg/sessions/u2net.py .

No images were sent to a remote annotation service. Product labels come from supplied metadata and masks were generated locally. Human annotation/review status is recorded explicitly.

## Uploaded ZIP audit (v3)

The uploaded Diya Roboflow archive states CC BY 4.0; its source is https://app.roboflow.com/ansh-shakya/diya-n10q1-vwdfp/1 . Box-prompted masks are derivative automatic annotations, retained as auxiliary correction candidates. The cloth-seg5 archive also states CC BY 4.0; its supplied notices remain under provenance and the auxiliary garment dataset. FMD material-region examples retain the supplied archive contents in `auxiliary/material_region_references`; missing licensing terms are not replaced with an assumed license. Full archive inventories, hashes, extracted notices and outcome counts are under `reports/zip_audit` and `provenance/zip_audit`. No original archive or sharing ZIP was changed.

## Targeted Wikimedia Commons additions (v2)

File-level author, source URL, license name and license URL are recorded in `external/candidates.csv` and `external/approved.csv`. These photographs were downloaded as thumbnails and re-encoded as JPEG for annotation. Preserve attribution and applicable share-alike terms. Candidate download does not mean a photo is included in training. See `external/visual_review.csv` and the dataset manifest. No new dataset or model license is granted over the source photographs.
