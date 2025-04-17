from ultralytics import YOLO

def load_model(weights_path="best.pt"):
    return YOLO(weights_path)
