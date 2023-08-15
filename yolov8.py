from ultralytics import YOLO
from datetime import datetime
import cv2
import time
import mod

model = YOLO("yolov8m.pt")
vid = cv2.VideoCapture(0)
start_time = time.time()
frame_count = 0
starting_time = time.time()
confidence = 0.281

while True:
    return_value, frame = vid.read()

    if not return_value:
        print("Failed to capture frame from webcam")
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    image_filename = './data/captured_frame.jpg'
    cv2.imwrite(image_filename, frame)
    frame_count += 1

    if time.time() - start_time >= 2:
        # test from GCR
        request_time = datetime.now()
        print('Request sent time: ', request_time)

        prediction = model(frame, conf=confidence)[0]
        data = prediction.boxes.data.tolist()
        texts = []
        lists = []
        for i in data:
            text, lis = mod.give_direction(i[:4], prediction.names[i[5]], frame)
            if len(text) != 0:
                texts.append(text)
            lists.append(lis)
        if len(texts) == 0:
            print("No object detected.")
        else:
            print(texts)
            # print(resp.json()["bbox"])
        receive_time = datetime.now()
        print('Response received: ', receive_time)
        print('RTT: ', receive_time - request_time)
        start_time = time.time()
    else:
        prediction = model(frame, conf=confidence)[0]
        data = prediction.boxes.data.tolist()
        lists = []
        for i in data:
            text, lis = mod.give_direction(i[:4], prediction.names[i[5]], frame)
            lists.append(lis)
    height, width, _ = frame.shape
    line1_pos = int(width * 20 / 100)
    line2_pos = int(width * 80 / 100)

    # Draw lines on the frame
    green = (0, 255, 0)
    black = (0, 0, 0)
    red = (0, 0, 255)

    #segmentation
    cv2.line(frame, (line1_pos, 0), (line1_pos, height), black, 3)
    cv2.line(frame, (line2_pos, 0), (line2_pos, height), black, 3)

    #drawing bounding boxes
    for lis in lists:
        if lis['location'] == 'straight':
            if lis['movable']:
                if lis['distance'] <= 5:
                    cv2.rectangle(frame, tuple(lis['bbox'][:2]), tuple(lis['bbox'][2:]), red, 1)
                    cv2.putText(frame, f"Object:{lis['object']}, Distance:{lis['distance']}, Location:{lis['location']}", tuple([lis['bbox'][0], lis['bbox'][1]]), 0, 0.5, black, 1)
            elif lis['distance'] <= 3:
                cv2.rectangle(frame, tuple(lis['bbox'][:2]), tuple(lis['bbox'][2:]), green, 1)
                cv2.putText(frame, f"Object:{lis['object']}, Distance:{lis['distance']}, Location:{lis['location']}", tuple([lis['bbox'][0], lis['bbox'][1]]), 0, 0.5, black, 1)
        elif lis['movable']:
            cv2.rectangle(frame, tuple(lis['bbox'][:2]), tuple(lis['bbox'][2:]), red, 1)
            cv2.putText(frame, f"Object:{lis['object']}, Distance:{lis['distance']}, Location:{lis['location']}", tuple([lis['bbox'][0], lis['bbox'][1]]), 0, 0.5, black, 1)

    cv2.imshow("Output Video", frame)
print("FPS: ", frame_count/(time.time()-starting_time))