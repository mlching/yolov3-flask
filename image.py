# image.py
import tensorflow as tf
from utils import load_class_names, output_boxes, give_direction, resize_image
import cv2
import numpy as np
from yolov3 import YOLOv3Net
import json

model_size = (416, 416,3)
num_classes = 80
class_name = 'data/coco.names'
max_output_size = 40
max_output_size_per_class= 20
iou_threshold = 0.5
confidence_threshold = 0.5
cfgfile = 'cfg/yolov3.cfg'
weightfile = 'yolov3_weights.tf'

# Average height and width of object classes
obj_height_width = {'person' : [1.7, 0.367],
                    'bicycle' : [1.676,0.54],
                    'car' : [1.828, 1.767],
                    'motorbike' : [1.524, 1.016],
                    'aeroplane' : [84.8, 88.4],
                    'bus' : [3.81, 2.55],
                    'train' : [4.025, 3.24],
                    'truck' : [1.940, 2.049],
                    'boat' : [0.46, 3.05],
                    'traffic light' : [0.762, 0.241],
                    'fire hydrant' : [0.762 , 0.355],
                    'stop sign' : [3.05, 0.5],
                    'parking meter' : [0.5, 0.2],
                    'bench' : [0.508, 0.381],
                    'bird' : [0.47, 0.35],
                    'cat' : [0.46, 0.64],
                    'dog' : [0.84, 1.07],
                    'horse' : [1.73, 1.90],
                    'sheep' : [1.17, 1.27],
                    'cow' : [1.8, 2.45],
                    'elephant' : [4, 5],
                    'bear' : [1.37, 2.44],
                    'zebra' : [1.91, 2.44],
                    'giraffe' : [6, 2.6],
                    'backpack' : [0.47, 0.23],
                    'umbrella' : [1.01, 1.30],
                    'handbag' : [0.23, 0.26],
                    'tie' : [0.508, 0.1],
                    'suitcase': [0.56, 0.38],
                    'frisbee' : [0.3, 0.3],
                    'skis' : [1.58, 0.2],
                    'snowboard' : [1.35, 0.2],
                    'sports ball' : [0.23, 0.23],
                    'kite' : [0.9, 0.8],
                    'baseball bat' : [0.02, 0.864],
                    'baseball glove' : [0.3, 0.24],
                    'skateboard' : [0.0889,0.1905],
                    'surfboard' : [2.194, 0.56],
                    'tennis racket' : [0.6096, 0.257],
                    'bottle' : [0.304, 0.081],
                    'wine glass' : [0.155, 0.065],
                    'cup' : [0.094, 0.08],
                    'fork' : [0.18, 0.10],
                    'knife' :[0.152, 0.044],
                    'spoon' : [0.16, 0.036],
                    'bowl' : [0.1, 0.3],
                    'banana' : [0.18, 0.03],
                    'apple' : [0.02, 0.02],
                    'sandwich' : [0.121, 0.121],
                    'orange' : [0.02, 0.02],
                    'broccoli' : [0.121, 0.121],
                    'carrot' : [0.18, 0.09],
                    'hot dog' : [0.18, 0.09],
                    'pizza' :  [0.02, 0.406],
                    'donut' : [0.0762, 0.20],
                    'cake' : [0.12, 0.4],
                    'chair': [1.009, 0.485],
                    'sofa': [0.84, 1.52],
                    'pottedplant' : [1.05, 0.28],
                    'bed' : [0.75, 0.46],
                    'diningtable': [0.787, 1.016],
                    'toilet' : [0.762, 0.735],
                    'tvmonitor': [0.340, 0.556],
                    'laptop': [0.209, 0.350],
                    'mouse' : [0.0381, 0.0855],
                    'remote' : [0.17, 0.035],
                    'keyboard' : [0.022, 0.022],
                    'cell phone' : [0.1436, 0.0709],
                    'microwave' : [0.313, 0.52],
                    'oven' : [0.72, 0.76],
                    'toaster' : [0.284, 0.345],
                    'sink' : [0.75, 0.61],
                    'refrigerator' : [1.82, 0.749],
                    'book' : [0.215, 0.139],
                    'clock' : [0.3, 0.3],
                    'vase' : [0.4, 0.1],
                    'scissors' : [0.1778, 0.10],
                    'teddy bear' : [0.304, 0.33],
                    'hair drier' : [0.28, 0.245],
                    'toothbrush' : [0.166, 0.0063]
                    }


def navigation(image):
    height, width, channels = image.shape
    image = np.array(image)
    image = tf.expand_dims(image, 0)
    resized_frame = resize_image(image, (model_size[0],model_size[1]))
    model = YOLOv3Net(cfgfile,model_size,num_classes)
    model.load_weights(weightfile)
    class_names = load_class_names(class_name)
    pred = model.predict(resized_frame)
    boxes, scores, classes, nums = output_boxes( \
        pred, model_size,
        max_output_size=max_output_size,
        max_output_size_per_class=max_output_size_per_class,
        iou_threshold=iou_threshold,
        confidence_threshold=confidence_threshold)
    image = np.squeeze(image)
    directions = give_direction(image, boxes, scores, classes, nums, class_names, obj_height_width)
    return json.dumps(directions)