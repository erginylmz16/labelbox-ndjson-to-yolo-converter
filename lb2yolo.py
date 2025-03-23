import json
import os

# Path to the LabelBox JSON export file
# This file contains image annotations exported from LabelBox platform
lb_ndjson_path = 'your_labelbox_export.ndjson_path'

# List of classes
# The index of each class in this list will be used as class_id in YOLO format
# Example: stop is at index 2, so it will be represented as class_id 2
labels = ["speed_limit_50km-h",
          "roundabout",
          "stop",]


all_results = []

def parse_labelbox_data(json_line):
    data = json.loads(json_line)
    
    image_name = data["data_row"]["external_id"]
    
    img_width = data["media_attributes"]["width"]
    img_height = data["media_attributes"]["height"]
    
    annotations = []
    
    project_key = list(data["projects"].keys())[0]
    labels = data["projects"][project_key]["labels"]
    
    if labels and len(labels) > 0:
        objects = labels[0]["annotations"]["objects"]
        
        for obj in objects:
            bbox = obj["bounding_box"]
            annotation = {
                "name": obj["name"],
                "bbox": {
                    "top": bbox["top"],
                    "left": bbox["left"],
                    "width": bbox["width"],
                    "height": bbox["height"]
                }
            }
            annotations.append(annotation)
    
    return {
        "image_name": image_name,
        "width": img_width,
        "height": img_height,
        "annotations": annotations
    }


with open(lb_ndjson_path, 'r') as file:
    for line in file:
        result = parse_labelbox_data(line)
        all_results.append(result)


os.makedirs('labels', exist_ok=True)

for result in all_results:
    image_name = result['image_name'].split('.')[0]
    
    txt_path = os.path.join('labels', f"{image_name}.txt")
    
    with open(txt_path, 'w') as f:
        for ann in result['annotations']:
            class_idx = labels.index(ann['name'])
            
            x = ann['bbox']['left'] / result['width']
            y = ann['bbox']['top'] / result['height']
            w = ann['bbox']['width'] / result['width']
            h = ann['bbox']['height'] / result['height']
            
            x_center = x + (w/2)
            y_center = y + (h/2)
            
            f.write(f"{class_idx} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")