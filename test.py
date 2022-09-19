import requests
from datetime import datetime
import cv2

#test from GCR
request_time = datetime.now()
print('Request sent time: ', request_time)
# resp = requests.post("https://yolov3-flask-wx2bjo7cia-uc.a.run.app", files={'file': open('data/Test_3.jpeg', 'rb')})

resp = requests.post("http://127.0.0.1:5000/", files={'file': open('data/Test_3.jpeg', 'rb')})
#test locally on image built on external drive
#resp = requests.post("http://0.0.0.0:5000", files={'file': open('../../../Documents/junkboatpic.jpg', 'rb')})

print(resp.json())
receive_time = datetime.now()
print('Response received: ', receive_time)
print('RTT: ', receive_time - request_time)