# AI Crowd Density Monitoring System
# 👥 AI Crowd Density Monitoring System

An AI-powered real-time crowd density monitoring system built using Python, OpenCV, and YOLOv8.

This project detects people in a video stream and classifies crowd density levels into Low, Medium, or High categories. It logs high-density events and captures evidence images for monitoring purposes.

Designed for:
- Smart city applications
- Public safety research
- AI & Computer Vision learning
- Engineering mini/major projects
- Hackathons

---

## 🚀 Features

- Real-time person detection
- Crowd density classification (Low / Medium / High)
- Automatic high-density alert logging
- Image capture for high-density events
- Webcam or video file support
- Lightweight YOLOv8 nano model

---

## 🧠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- NumPy

---

## 📂 Project Structure

AI_Crowd_Density_Monitoring_System/
│
├── main.py
├── detector.py
├── config.py
├── requirements.txt
├── logs/
├── captures/
└── README.md

---

## ⚙️ Installation

1. Install Python 3.10 or later.
2. Clone the repository:

   git clone <your-repository-link>

3. Navigate to the project directory:

   cd AI_Crowd_Density_Monitoring_System

4. Install dependencies:

   pip install -r requirements.txt

5. Run the system:

   python main.py

The YOLOv8 model will automatically download on first execution.

---

## 📊 How It Works

1. Video stream is captured from webcam or file.
2. YOLOv8 detects persons in each frame.
3. Total person count is calculated.
4. Density level is classified:
   - Low (Below threshold)
   - Medium (Moderate crowd)
   - High (Above threshold)
5. When High density is detected:
   - Event is logged in `/logs`
   - Image evidence is saved in `/captures`

---

## 🖥 System Requirements

Minimum:
- Windows 11
- 8GB RAM
- Webcam or video input

Recommended:
- NVIDIA GPU for faster inference

---

## ⚠️ Current Limitation

This version uses frame-based counting and does not include tracking.
Temporary detection loss may affect density classification.

Future improvements:
- Object tracking integration (DeepSORT)
- Crowd heatmap visualization
- Real-time analytics dashboard
- CSV data export
- Alert notifications (Email/Telegram)

---

## 🔒 Ethical & Legal Notice

This project is intended for educational and research purposes only.
Ensure compliance with privacy and surveillance regulations before real-world deployment.

---

## 👨‍💻 Author

Developed as an AI-based crowd monitoring simulation project.

Real-time crowd density monitoring using YOLOv8 and OpenCV.

## Features
- Real-time person detection
- Crowd density classification (Low / Medium / High)
- High-density event logging
- Automatic image capture
- Webcam or video input support

## Setup

1. Install Python 3.10+
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python main.py

YOLO model will auto-download on first run.
