import cv2
from ultralytics import YOLO
import torch.serialization

from torch.nn.modules.container import Sequential, ModuleList
from torch.nn.modules.pooling import MaxPool2d
from torch.nn import Conv2d, BatchNorm2d, SiLU
from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.modules.conv import Conv
from ultralytics.nn.modules.block import C2f, Bottleneck, SPPF
from torch.nn.modules.upsampling import Upsample
from ultralytics.nn.modules.conv import Concat
from ultralytics.nn.modules.head import Detect
from ultralytics.nn.modules.block import DFL
from ultralytics.yolo.utils import IterableSimpleNamespace
from ultralytics.yolo.utils.loss import v8DetectionLoss, BboxLoss
from torch.nn.modules.loss import BCEWithLogitsLoss
from ultralytics.yolo.utils.tal import TaskAlignedAssigner

# Registro seguro para cargar modelos
torch.serialization.add_safe_globals([
    Sequential, ModuleList,
    Conv2d, BatchNorm2d, SiLU,
    DetectionModel, Conv,
    C2f, Bottleneck, SPPF,
    MaxPool2d, Upsample,
    Concat, Detect, DFL,
    IterableSimpleNamespace,
    v8DetectionLoss,
    BCEWithLogitsLoss,
    TaskAlignedAssigner,
    BboxLoss
])

# Cargar el modelo entrenado
model = YOLO("license_plate_detector.pt", task='detect')


def detect_plates(img):
    results = model(img)[0]  # ⬅️ Accede al primer resultado

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
