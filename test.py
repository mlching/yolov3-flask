import requests
from datetime import datetime
import cv2
import time


# Initialize the webcam
video_path = "./data/test.mp4"
vid = cv2.VideoCapture(0)
start_time = time.time()


while True:
    return_value, frame = vid.read()

    if not return_value:
        print("Failed to capture frame from webcam")
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() - start_time >= 2:

        image_filename = './data/captured_frame.jpg'
        cv2.imwrite(image_filename, frame)
        
        #test from GCR
        request_time = datetime.now()
        print('Request sent time: ', request_time)
        # resp = requests.post("https://yolov3-flask-wx2bjo7cia-uc.a.run.app", files={'file': open('data/Test_3.jpeg', 'rb')})

        resp = requests.post("http://127.0.0.1:5000/", files={'file': open(image_filename, 'rb')})
        #test locally on image built on external drive
        #resp = requests.post("http://0.0.0.0:5000", files={'file': open('../../../Documents/junkboatpic.jpg', 'rb')})
        if resp.json() == {'error': "cannot access local variable 'mytext' where it is not associated with a value"}:
            print("No object detected.")
        else:
            print(resp.json())
        receive_time = datetime.now()
        print('Response received: ', receive_time)
        print('RTT: ', receive_time - request_time)
        start_time = time.time()
    height, width, _ = frame.shape
    line1_pos = int(width * 33 / 100)  
    line2_pos = int(width * 67 / 100)  

    # Draw lines on the frame
    line_color = (0, 255, 0)  # Green color
    line_thickness = 2
    cv2.line(frame, (line1_pos, 0), (line1_pos, height), line_color, line_thickness)
    cv2.line(frame, (line2_pos, 0), (line2_pos, height), line_color, line_thickness)
    cv2.imshow("Output Video", frame)
    

