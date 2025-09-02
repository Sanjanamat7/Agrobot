# 🌱 Agrobot

Agrobot is an AI-powered agriculture assistant that uses **YOLO (You Only Look Once)** object detection to identify plants, leaves, and diseases in real time.  
It supports running detection via webcam and also includes trained YOLO models for agricultural tasks.

---

## 📂 Repository Structure
- `webcam_yolo.py` → Script to run real-time detection using webcam  
- `Untitled0.ipynb` → Jupyter notebook for model training/experimentation  
- `best.pt` → Custom-trained YOLO model weights  
- `yolo11n.pt`, `yolov8n.pt` → Pretrained YOLO model weights  

---

## ⚙️ Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/Sanjanamat7/Agrobot.git
cd Agrobot
```
### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
### 3. Install dependencies
```bash
pip install ultralytics opencv-python torch torchvision
```
## ▶️ How to Run
Run YOLO Detection on Webcam
```bash
python webcam_yolo.py
```
