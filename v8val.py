# Load YOLOv8n, train it on COCO128 for 3 epochs and predict an image with it
from ultralytics import YOLO
import csv

model_name = "yolov3-tinyu"
model = YOLO(f'{model_name}.pt')  # load a pretrained YOLOv8n detection model
#model.train(data='coco128.yaml', epochs=3)  # train the model
#val = model.val(data='project-1.yaml')
val = model.val(data='coco128.yaml')
csv_file = open('val_results_coco128.csv', mode='a', newline='')
#csv_file = open('val_results_testing2.csv', mode='a', newline='')
csv_writer = csv.writer(csv_file)
#csv_writer.writerow(["model_name", 'metrics/precision(B)', 'metrics/recall(B)', 'metrics/mAP50(B)', 'metrics/mAP50-95(B)', 'fitness'])
lis = [model_name]
for i in val.results_dict:
    lis.append(val.results_dict[i])
print(lis)
csv_writer.writerow(lis)
