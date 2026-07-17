# 🎮 AI Virtual Game Controller

> **An AI-powered Human–Computer Interaction System for Real-Time Gesture-Based Game Control**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![AI](https://img.shields.io/badge/Artificial-Intelligence-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📖 Overview

**AI Virtual Game Controller** is a Final Year Engineering Project that enables users to control keyboard-based games using **real-time hand gestures** instead of traditional input devices.

The system combines **Computer Vision**, **Artificial Intelligence**, and **Machine Learning** to recognize hand movements through a webcam and convert them into game actions with high accuracy and low latency.

This project demonstrates the practical implementation of modern AI technologies for **Human–Computer Interaction (HCI)**.

---

# 🎯 Project Objectives

- Develop a touchless game control system.
- Replace keyboard input with natural hand gestures.
- Demonstrate AI-based gesture recognition.
- Build a modular and scalable software architecture.
- Achieve real-time performance with low latency.

---

# ✨ Features

## AI Features

- Real-Time Hand Detection
- AI Gesture Recognition
- Adaptive Motion Threshold Engine
- Gesture Smoothing Engine
- Confidence-Based Prediction
- Motion Trail Tracking

---

## System Features

- Automatic Camera Recovery
- Performance Monitoring
- FPS Counter
- CPU & RAM Monitoring
- Runtime Statistics
- Professional Dashboard

---

## Software Features

- Modular Architecture
- Object-Oriented Design
- Easy Configuration
- Extensible AI Pipeline
- Professional UI

---

# 🖐 Supported Gestures

| Gesture | Action |
|----------|--------|
| Move Left | ⬅ LEFT |
| Move Right | ➡ RIGHT |
| Move Up | ⬆ JUMP |
| Move Down | ⬇ SLIDE |
| Open Palm | ⏸ PAUSE |

---

# 🏗 Software Architecture

```
Web Camera
     │
     ▼
Hand Detector
     │
     ▼
Gesture Detector
     │
     ▼
Adaptive Threshold
     │
     ▼
Gesture Smoother
     │
     ▼
AI Core
     │
     ▼
Game Controller
     │
     ▼
Keyboard Controller
```

---

# 📂 Project Structure

```
AI_Virtual_Game_Controller/
│
├── ai/
│   ├── ai_core.py
│   ├── adaptive_threshold.py
│   ├── ai_statistics.py
│   └── gesture_smoother.py
│
├── controllers/
│   ├── game_controller.py
│   └── keyboard_controller.py
│
├── detectors/
│   ├── hand_detector.py
│   └── gesture_detector.py
│
├── monitoring/
│   ├── camera_recovery.py
│   ├── performance_monitor.py
│   └── system_info.py
│
├── ui/
│   ├── dashboard.py
│   ├── dashboard_panel.py
│   ├── cards.py
│   ├── theme.py
│   └── ui.py
│
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── ABOUT.md
```

---

# 🧠 Technologies Used

## Programming Language

- Python 3.11.x

## Computer Vision

- OpenCV
- MediaPipe Hands

## Artificial Intelligence

- Gesture Classification
- Adaptive Thresholding
- Gesture Smoothing
- Motion Analysis

## System Monitoring

- psutil

---

# ⚙ Installation

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt

# #  Verify Installation

```bash
python -c "import cv2;print(cv2.__version__)"
python -c "import mediapipe as mp;print(mp.__version__)"
python -c "import psutil;print(psutil.__version__)"
python -c "import pynput;print('Pynput OK')"

## Clone Repository

```bash
git clone https://github.com/purva008/AI-Virtual-Game-Controller.git
```

---

## Navigate to Project

```bash
cd AI-Virtual-Game-Controller
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

```bash
python main.py
```

---

# 📊 Dashboard Information

The professional dashboard displays:

- Current Gesture
- FPS
- Average FPS
- Runtime
- CPU Usage
- RAM Usage
- Camera Status
- AI Confidence
- Motion Trail
- Bounding Box

---

# 🔧 Configuration

All application settings are managed through:

```
config.py
```

Example:

```python
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

MOTION_COOLDOWN = 0.25

HISTORY_SIZE = 10

MINIMUM_VOTES = 6
```

---

# 🧪 Testing

Verify:

- Webcam detection
- Hand detection
- Gesture recognition
- Dashboard updates
- Keyboard actions
- Camera recovery
- FPS stability

---

# 📈 Future Enhancements

- Deep Learning Gesture Recognition
- Custom Gesture Training
- Voice Commands
- Multi-Hand Support
- Multiplayer Mode
- Game Profiles
- Mobile Camera Integration
- Gesture Recording
- AI Personalization

---

# 📚 Academic Contribution

This project demonstrates practical implementation of:

- Artificial Intelligence
- Computer Vision
- Human Computer Interaction
- Software Engineering
- Object-Oriented Programming
- Real-Time Systems

---

# 👨‍💻 Developer

**Purva Ahire**

---

# 📜 License

This project is developed for **academic and research purposes**

© 2026 Purva Ahire  
All Rights Reserved.

---

# ⭐ Acknowledgements

Special thanks to:

- OpenCV Community
- Google MediaPipe
- Python Community
- Faculty and Project Guide
- Open Source Contributors

---

# 📬 Contact

For academic discussions or project-related queries:

**Developer:** Purva Ahire

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub.