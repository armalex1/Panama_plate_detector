# License Plate Recognition Web App (Panama 🇵🇦)

This is a web-based license plate recognition system built with Python, FastAPI, and EasyOCR.  
It allows real-time detection of vehicle plates using the user's webcam, and compares detected plates against a user-uploaded Excel file containing authorized plates.

---

## 🚀 Features

- Real-time plate detection using webcam(s)
- OCR powered by EasyOCR
- Excel upload for authorized plate list
- Downloadable Excel template
- Multicamera support from browser (with manual or automatic selection)
- Fully web-based: no installation required for end users
- Adapted to Panama license plate formats

---

## ⚙️ Technologies Used

- Python 3.12+
- FastAPI
- EasyOCR
- OpenCV
- Uvicorn
- HTML + JavaScript (Frontend)

---

## 💻 Local Installation

1. Clone this repository  
   `git clone https://github.com/yourusername/plate-tracker.git && cd plate-tracker`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the server  
   `uvicorn main:app --reload`

4. Open your browser  
   Go to [http://localhost:8000](http://localhost:8000)

---

## 🌐 Deploy on Render.com

1. Push your code to a GitHub repository.
2. Create a new Web Service on [Render](https://render.com/).
3. Use the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - **Environment**: Python 3.12
4. Add `static/` folder and optional Excel template in root.

---

## 📄 License

MIT License

---

## 📬 Contact

Project by [Armando Vegas](mailto:es.armandovegas@gmail.com)  
Inspired by real-world needs in Panama for smarter vehicle access and verification.
