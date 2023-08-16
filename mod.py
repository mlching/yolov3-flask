
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

def distance_one(focal_length, Orig_height_width, Img_height, Img_width):
    alpha = Img_height/Orig_height_width[0]
    beta = (Img_height * Img_width) / (Orig_height_width[0] * Orig_height_width[1])
    far = False
    distance = 0
    if (Img_height < (alpha-alpha/2)) and ((Img_height * Img_width) > (beta+beta/2)):
        distance = 0.5
    elif (Img_height < (alpha-alpha/2)) or (Img_height > (alpha+alpha/2)) and ((Img_height * Img_width) > (beta/3)):
        distance = (focal_length * 100 * Orig_height_width[0])/Img_height
        far = True
        #distance = 100
    elif ((alpha-alpha/2) <= Img_height <= (alpha+alpha/2)) and (1000 <= (Img_height * Img_width) <= (beta+beta/2)):
        distance = (focal_length * 100 * Orig_height_width[0])/Img_height
    #print(f"Img_height: {Img_height}, Img_area: {Img_height * Img_width}, alpha: {alpha}, beta: {beta}, far: {far}, distance: {distance}")
    return round(distance, 4)

def give_direction(boxes, classes, img):
    x1 = round(boxes[0])
    x2 = round(boxes[2])
    y1 = round(boxes[1])
    y2 = round(boxes[3])

    obj_height_width = {'person' : [1.7, 0.367],
                    'bicycle' : [1.676,0.54],
                    'car' : [1.828, 1.767],
                    'motorcycle' : [1.524, 1.016],
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
                    'couch': [0.84, 1.52],
                    'potted plant' : [1.05, 0.28],
                    'bed' : [0.75, 0.46],
                    'dining table': [0.787, 1.016],
                    'toilet' : [0.762, 0.735],
                    'tv': [0.340, 0.556],
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
    movable_objects = ["person", "bicycle", "car", "motorcycle", "aeroplane",
                   "bus", "train", "truck", "boat", "bird", "cat", "elephant",
                   "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra"
                   "giraffe"]

    height_obj = abs(y2-y1)
    width_obj = abs(x2-x1)
    center_x = x1 + width_obj/2

    location = object_location(img.shape[1], center_x)
    first_distance = distance_one(3.543, obj_height_width[classes], height_obj, width_obj)

    lis = {'object': classes, 'distance': first_distance, 'location': location, 'bbox': [x1, y1, x2, y2], 'movable': False}
    if classes in movable_objects:
        lis['movable'] = True
    texts = []
    #middle
    if lis['location'] == 'straight':
            if lis['object'] in movable_objects:
                if 0.8 <= lis['distance'] <= 5:
                    mytext = "There is a "+lis['object']+" at "+str(round(lis['distance'], 1))+" meters ahead of you."
                    texts.append(mytext)
            elif 0.8 <= lis['distance'] <= 3:
                mytext = "There is a "+lis['object']+" at "+str(round(lis['distance'], 1))+" meters ahead of you."
                texts.append(mytext)
            elif lis['distance'] <0.8:
                mytext = "There is a " + lis['object'] + " less than a meter ahead of you."
                texts.append(mytext)

    #sides
    elif lis['object'] in movable_objects:
        if 5.0 >= lis['distance'] >= 0.8:
            mytext = "There is a "+lis['object']+" at "+str(round(lis['distance'], 1))+" meters to your "+lis['location'] + "."
        elif lis['distance'] > 5.0:
            mytext = "There is a " + lis['object'] + " greater than 5 meters to your "+lis['location'] + "."
        else:
            mytext = "There is a " + lis['object'] + " less than a meter to your " +lis['location'] + "."
        texts.append(mytext)
    return texts, lis