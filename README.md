# License Plate Recognition Web App (Panama 🇵🇦)

Este es un sistema web de reconocimiento de placas vehiculares desarrollado con Python, FastAPI y EasyOCR.  
Permite la detección en tiempo real de placas mediante cámara web, comparación contra una lista cargada en Excel, y registro de resultados con geolocalización y exportación de logs.

---

## 🚀 Funcionalidades

- Detección en tiempo real de placas desde la cámara
- Soporte para múltiples cámaras seleccionables
- OCR con EasyOCR y mejoras de imagen con OpenCV
- Carga de archivo Excel con placas autorizadas
- Plantilla de Excel descargable para facilitar la carga
- Visualización de resultados en una tabla interactiva
- Geolocalización automática desde el navegador
- Enlaces directos a Google Maps por cada detección
- Exportación de registros visibles en tabla a CSV
- Regeneración automática del log al iniciar sesión

---

## ⚙️ Tecnologías Utilizadas

- Python 3.12+
- FastAPI
- EasyOCR
- OpenCV
- Uvicorn
- HTML5 + JavaScript (Frontend)

---

## 💻 Instalación Local

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/yourusername/plate-tracker.git && cd plate-tracker
   ```

2. Instala las dependencias:  
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el servidor:  
   ```bash
   uvicorn main:app --reload
   ```

4. Abre tu navegador:  
   [http://localhost:8000](http://localhost:8000)

---

## 🌐 Despliegue en Render.com

1. Sube tu código a GitHub.
2. Crea un nuevo servicio web en [Render](https://render.com/).
3. Configuración sugerida:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - **Python Version**: 3.12
4. Incluye la carpeta `static/` y el archivo `template.xlsx` en la raíz.

---

## 📁 Estructura de Carpetas

```
├── main.py                # Servidor FastAPI principal
├── static/                # Archivos estáticos (HTML, JS, imágenes)
├── processing.py          # Detección de placas con OpenCV
├── ocr.py                 # OCR y extracción de texto
├── verifier.py            # Comparación contra Excel
├── uploaded_plates.xlsx   # Archivo cargado con placas válidas
├── placas_detectadas_log.xlsx  # Log de detecciones
├── template.xlsx          # Plantilla de ejemplo para carga de placas
├── requirements.txt       # Dependencias del proyecto
```

---

## 📄 Licencia

MIT License

---

## 📬 Contacto

Proyecto desarrollado por [Armando Vegas](mailto:es.armandovegas@gmail.com)  
Inspirado en necesidades reales para el control de acceso vehicular en Panamá y Latinoamérica.
