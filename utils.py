import tensorflow as tf
import numpy as np
import cv2
import time

movable_objects = ["person", "bicycle", "car", "motorbike", "aeroplane",
                   "bus", "train", "truck", "boat", "bird", "cat", "elephant",
                   "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra"
                   "giraffe"]

# Calculates the diatnce of an object in the image using focal length of camera
def distance_one(focal_length, Orig_height, Img_height):
    distance = (focal_length * 100 * Orig_height)/Img_height
    return round(distance, 4)

# Determines the location of an object in the image
def object_location(img_width, x_center):
    image_center = img_width/2
    location = None
    if x_center >= (img_width - (img_width/100)* 20):
        location = 'right'
    elif x_center <= (img_width/100)* 20:
        location = 'left'
    else:
        location = 'straight'
    return location

def non_max_suppression(inputs, model_size, max_output_size,
                        max_output_size_per_class, iou_threshold,
                        confidence_threshold):
    bbox, confs, class_probs = tf.split(inputs, [4, 1, -1], axis=-1)
    bbox=bbox/model_size[0]
    scores = confs * class_probs
    boxes, scores, classes, valid_detections = \
        tf.image.combined_non_max_suppression(
        boxes=tf.reshape(bbox, (tf.shape(bbox)[0], -1, 1, 4)),
        scores=tf.reshape(scores, (tf.shape(scores)[0], -1,
                                   tf.shape(scores)[-1])),
        max_output_size_per_class=max_output_size_per_class,
        max_total_size=max_output_size,
        iou_threshold=iou_threshold,
        score_threshold=confidence_threshold
    )
    return boxes, scores, classes, valid_detections

def resize_image(inputs, modelsize):
    inputs= tf.image.resize(inputs, modelsize)
    return inputs

def load_class_names(file_name):
    with open(file_name, 'r') as f:
        class_names = f.read().splitlines()
    return class_names

def output_boxes(inputs,model_size, max_output_size, max_output_size_per_class,
                 iou_threshold, confidence_threshold):
    center_x, center_y, width, height, confidence, classes = \
        tf.split(inputs, [1, 1, 1, 1, 1, -1], axis=-1)
    top_left_x = center_x - width / 2.0
    top_left_y = center_y - height / 2.0
    bottom_right_x = center_x + width / 2.0
    bottom_right_y = center_y + height / 2.0
    inputs = tf.concat([top_left_x, top_left_y, bottom_right_x,
                        bottom_right_y, confidence, classes], axis=-1)
    boxes_dicts = non_max_suppression(inputs, model_size, max_output_size,
                                      max_output_size_per_class, iou_threshold, confidence_threshold)
    return boxes_dicts

def give_direction(img, boxes, objectness, classes, nums, class_names, obj_height_width):
    boxes, objectness, classes, nums = boxes[0], objectness[0], classes[0], nums[0]
    boxes = np.array(boxes)
    lists = []
    for i in range(nums):
        category = class_names[int(classes[i])]
        if  category in obj_height_width.keys():
            dist = {'object': None, 'distance': None, 'location': None, 'bbox': None, 'movable': False, 'confidence': objectness.numpy().tolist()[i]}

            x1y1 = tuple((boxes[i,0:2] * [img.shape[1],img.shape[0]]).astype(np.int32))
            x2y2 = tuple((boxes[i,2:4] * [img.shape[1],img.shape[0]]).astype(np.int32))

            height_obj = abs(x1y1[1] - x2y2[1])
            width_obj = abs(x2y2[0] - x1y1[0])
            center_x = x1y1[0]+ width_obj/2
            center_y = x2y2[0] + height_obj/2
            
            location = object_location(img.shape[1], center_x)
            first_distance = distance_one(3.543, obj_height_width[category][0], height_obj)

            dist['object'] = category
            dist['distance'] = first_distance
            dist['location'] = location
            dist['bbox'] = np.array([x1y1, x2y2]).tolist()
            if category in movable_objects:
                dist['movable'] = True
            lists.append(dist)
    texts = []
    for lis in lists:
        if lis['location'] == 'straight':
            if lis['object'] in movable_objects:
                if lis['distance'] <= 5:
                    mytext = "There is a "+lis['object']+" at "+str(round(lis['distance'], 1))+" meters ahead of you."
                    texts.append(mytext)
            elif lis['distance'] <= 3:
                mytext = "There is a "+lis['object']+" at "+str(round(lis['distance'], 1))+" meters ahead of you."
                texts.append(mytext)
        elif lis['object'] in movable_objects:
            mytext = "There is a "+lis['object']+" at "+str(round(lis['distance'], 1))+" meters to your "+lis['location'] + "."
            texts.append(mytext)
    return texts, lists
