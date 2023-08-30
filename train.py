from ultralytics import YOLO

# Load a model
model = YOLO('yolov8m.yaml')
model = YOLO('yolov8m.pt')# build a new model from YAML
model = YOLO('yolov8m.yaml').load('yolov8m.pt')
# Train the model

if __name__ == '__main__':
    result = model.train(data='custom1and3.yaml', epochs=100, imgsz=640, batch=16, pretrained=True, val=True)
    result.val()