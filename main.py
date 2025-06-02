from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil
import cv2
import numpy as np
import easyocr
from processing import detect_plates, enhance_plate_image
from ocr import read_plate_text, extract_valid_plate
from verifier import load_plates_from_excel, check_plate

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

reader = easyocr.Reader(['en'])
UPLOAD_PATH = Path("uploaded_plates.xlsx")
TEMPLATE_PATH = Path("template.xlsx")


def load_active_plate_list():
    if UPLOAD_PATH.exists():
        return load_plates_from_excel(str(UPLOAD_PATH))
    return load_plates_from_excel("placas.xlsx")


@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    print("📸 Imagen recibida")

    results = []
    rects = detect_plates(img)
    print(f"🔍 Rectángulos detectados: {len(rects)}")

    plate_list = load_active_plate_list()

    for (x, y, w, h) in rects:
        cropped = img[y:y+h, x:x+w]
        enhanced = enhance_plate_image(cropped)
        raw_text = read_plate_text(reader, enhanced)
        print(f"🧠 OCR Result: {raw_text}")
        plate = extract_valid_plate(raw_text)
        if plate:
            found = check_plate(plate, plate_list)
            results.append({"plate": plate, "authorized": found})

    return {"results": results}


@app.post("/upload-plates")
async def upload_plates(file: UploadFile = File(...)):
    try:
        with open(UPLOAD_PATH, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


@app.get("/template")
async def get_template():
    if not TEMPLATE_PATH.exists():
        return {"error": "Template file not found."}
    return FileResponse(
        TEMPLATE_PATH,
        media_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
        filename="template.xlsx"
    )
