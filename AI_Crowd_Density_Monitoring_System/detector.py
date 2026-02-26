from ultralytics import YOLO
from config import TARGET_CLASS, CONFIDENCE_THRESHOLD

model = YOLO("yolov8n.pt")

def detect(frame):
    results = model(frame, verbose=False)[0]
    count = 0
    boxes = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        confidence = float(box.conf[0])

        if label == TARGET_CLASS and confidence > CONFIDENCE_THRESHOLD:
            count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            boxes.append((x1, y1, x2, y2))

    return count, boxes
