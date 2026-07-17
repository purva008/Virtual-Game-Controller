# 🎮 AI Virtual Game Controller using Hand Gesture Recognition

> A real-time AI-powered hand gesture recognition system that enables users to play **Temple Run** without touching the keyboard. The project uses Computer Vision and Artificial Intelligence to detect hand movements and convert them into game controls.

---

## 📌 Overview

The AI Virtual Game Controller is a Final Year Engineering Project developed using Python, OpenCV, and MediaPipe.

The system tracks the user's hand through a webcam, recognizes predefined gestures, processes them through an AI-based gesture pipeline, and converts them into keyboard commands for controlling the Temple Run game.

Instead of pressing keyboard keys, players simply move their hand in front of the camera.

---

## 🚀 Features

- Real-time hand tracking
- AI-based gesture recognition
- Gesture smoothing using majority voting
- Adaptive threshold algorithm
- Temple Run integration
- Professional dashboard
- Live FPS monitoring
- Camera recovery system
- System information monitoring
- Modular software architecture
- Easy to extend for future AI modules

---

## 🎯 Supported Temple Run Controls

| Hand Gesture | Game Action |
|--------------|-------------|
| Move Left | Left Arrow |
| Move Right | Right Arrow |
| Move Up | Jump |
| Move Down | Slide |
| Open Palm | Pause |

---

## 🧠 AI Pipeline

```
Camera
      │
      ▼
Hand Detection
      │
      ▼
Landmark Extraction
      │
      ▼
Motion Analysis
      │
      ▼
Adaptive Threshold
      │
      ▼
Gesture Smoothing
      │
      ▼
AI Core Engine
      │
      ▼
Temple Run Controller
```

---

## 🏗 Project Structure

```
Virtual-Game-Controller/
│
├── src/
│   ├── ai/
│   ├── controllers/
│   ├── detectors/
│   ├── system/
│   ├── ui/
│   ├── logger/
│   ├── main.py
│   └── config.py
│
├── assets/
├── docs/
├── README.md
├── ABOUT.md
└── requirements.txt
```

---

## 🛠 Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- psutil
- TensorFlow Lite (MediaPipe backend)

---

## ▶️ Installation

Clone the repository:

```bash
git clone <https://github.com/purva008/Virtual-Game-Controller>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/main.py
```

---

## 🎮 Usage

1. Launch Temple Run.
2. Run the application.
3. Allow webcam access.
4. Stand in front of the camera.
5. Perform gestures to control the game.

---

## 📈 Future Scope

- Deep Learning gesture prediction
- Gesture personalization
- Dynamic gesture training
- Voice + gesture hybrid controller
- Multi-player gesture control
- VR/AR interaction support

---

## 👩‍💻 Developer

**Purva Ahire**

Final Year Engineering Project

Artificial Intelligence | Computer Vision | Human Computer Interaction

---

## 📄 License

This project is developed for academic and educational purposes.