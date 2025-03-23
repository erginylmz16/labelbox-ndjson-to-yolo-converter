# LabelBox to YOLO Converter

A Python script to convert object detection annotations from LabelBox NDJSON format to YOLO format.

## Description

This tool converts bounding box annotations exported from LabelBox platform into YOLO format, which is widely used for training object detection models. The script handles the conversion of coordinates and creates individual annotation files for each image in YOLO format.

## Features

- Converts LabelBox NDJSON export to YOLO format
- Supports multiple classes
- Maintains aspect ratios and relative coordinates
- Creates a separate .txt file for each image
- Handles bounding box conversions automatically

## Prerequisites

- Python 3.x
- NDJSON export file from LabelBox

## Usage

1. Export your annotations from LabelBox in NDJSON format
2. Update the `lb_ndjson_path` variable in the script with your NDJSON file path
3. Modify the `labels` list to match your project's classes
4. Run the script:

```bash
python lb2yolo.py
```
## YOLO Format
The output files follow the YOLO format:

`<class_id> <x_center> <y_center> <width> <height>`

## Contributing

All contributions, big or small, are highly appreciated!

## License
MIT License
