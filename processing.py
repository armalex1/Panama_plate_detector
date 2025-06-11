import cv2
from ultralytics import YOLO

# Cargar el modelo YOLO entrenado
model = YOLO("license_plate_detector.pt")


def detect_plates(img):
    # Ejecutar inferencia
    results = model(img)[0]  # Primer resultado del batch

    rects = []
    for box in results.boxes.xyxy.cpu().numpy():
        x1, y1, x2, y2 = map(int, box[:4])
        w, h = x2 - x1, y2 - y1
        rects.append((x1, y1, w, h))
    return rects


def enhance_plate_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast = clahe.apply(gray)
    _, binarized = cv2.threshold(
        contrast, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    resized = cv2.resize(
        binarized, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR
    )
    return resized
