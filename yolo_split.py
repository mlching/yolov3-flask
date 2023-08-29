import json
import os
import shutil
from urllib.parse import unquote
import random

yolo = {"person": "0", "bicycle": "1", "car": "2", "motorcycle": "3", "airplane": "4", "bus": "5", "train": "6", "truck": "7", "boat": "8", "traffic light": "9", "fire hydrant": "10", "stop sign": "11", "parking meter": "12", "bench": "13", "bird": "14", "cat": "15", "dog": "16", "horse": "17", "sheep": "18", "cow": "19", "elephant": "20", "bear": "21", "zebra": "22", "giraffe": "23", "backpack": "24", "umbrella": "25", "handbag": "26", "tie": "27", "suitcase": "28", "frisbee": "29", "skis": "30", "snowboard": "31", "sports ball": "32", "kite": "33", "baseball bat": "34", "baseball glove": "35", "skateboard": "36", "surfboard": "37", "tennis racket": "38", "bottle": "39", "wine glass": "40", "cup": "41", "fork": "42", "knife": "43", "spoon": "44", "bowl": "45", "banana": "46", "apple": "47", "sandwich": "48", "orange": "49", "broccoli": "50", "carrot": "51", "hot dog": "52", "pizza": "53", "donut": "54", "cake": "55", "chair": "56", "couch": "57", "potted plant": "58", "bed": "59", "dining table": "60", "toilet": "61", "tv": "62", "laptop": "63", "mouse": "64", "remote": "65", "keyboard": "66", "cell phone": "67", "microwave": "68", "oven": "69", "toaster": "70", "sink": "71", "refrigerator": "72", "book": "73", "clock": "74", "vase": "75", "scissors": "76", "teddy bear": "77", "hair drier": "78", "toothbrush": "79", "minibus": "80", "telephone booth": "81", "taxi": "82", "handrail": "83", "ramp access": "84", "tactile paving": "85", "letter box": "86", "tram": "87", "tram station": "88", "bus stop": "89", "escalator": "90", "elevator": "91", "crosswalk": "92", "ATM": "93"}

def convert_to_yolo_format(obj, image_width, image_height):
    class_id = obj['rectanglelabels'][0]  # Replace spaces with underscores
    
    x_center = obj['x'] + obj['width'] / 2
    y_center = obj['y'] + obj['height'] / 2
    x_center /= image_width
    y_center /= image_height
    
    width = obj['width'] / image_width
    height = obj['height'] / image_height
    return f"{yolo[class_id]} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"

with open("custom4.json", "r") as f:
    data = json.load(f)

image_folder = "images"
txt_folder = "labels"
os.makedirs(image_folder, exist_ok=True)
os.makedirs(txt_folder, exist_ok=True)

"""
train_folder = "./labels/train_data"
val_folder = "./labels/val_data"
test_folder = "./labels/test_data"
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

train_folder = "./images/train_data"
val_folder = "./images/val_data"
test_folder = "./images/test_data"
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
"""

train_folder = "train_data"
val_folder = "val_data"
test_folder = "test_data"

# Shuffle the data
random.shuffle(data)

# Determine split ratios
train_ratio = 0.9  
val_ratio = 0.05  
test_ratio = 0.05  

total_samples = len(data)
train_samples = int(total_samples * train_ratio)
val_samples = int(total_samples * val_ratio)
test_samples = total_samples - train_samples - val_samples

train_data = data[:train_samples]
val_data = data[train_samples:train_samples + val_samples]
test_data = data[train_samples + val_samples:]

def process_dataset(dataset, folder):
    for annotation in dataset:
        image_name = os.path.basename(unquote(annotation['image'].split("/")[-1]))
        yolo_lines = []
        try:
            image_width = annotation['label'][0]['original_width']  # Assuming all objects have the same image dimensions
            image_height = annotation['label'][0]['original_height']
            

            for obj in annotation['label']:
                yolo_line = convert_to_yolo_format(obj, image_width, image_height)
                yolo_lines.append(yolo_line)
        except KeyError:
            print(f"{annotation['id']} has no label")

        image_path = os.path.join(image_folder, folder, f"{annotation['id']}.jpg")
        txt_path = os.path.join(txt_folder, folder, f"{annotation['id']}.txt")
        # Copy image to the image folder
        unix_path = annotation['image'].replace("/?d=", "/").replace("%5C", "/")
        windows_path = unix_path.replace("/data/local-files", "").replace("/", "\\")
        windows_path.replace("\\", "/")
        shutil.copy(windows_path, image_path)
        
        
        # Save image to the image folder
        # (You need to provide a way to save or copy the image file to this location)
        
        with open(txt_path, 'w') as f:
            f.write("\n".join(yolo_lines))
process_dataset(train_data, train_folder)
process_dataset(val_data, val_folder)
process_dataset(test_data, test_folder)