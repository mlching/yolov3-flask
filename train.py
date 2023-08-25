from ultralytics import YOLO

# Load a model
model = YOLO('yolov8m.yaml')  # build a new model from YAML
# Train the model

if __name__ == '__main__':
    result = model.train(data='custom1and3.yaml', epochs=100, imgsz=640, batch=16, pretrained=False)
    result.val()