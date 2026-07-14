# 🎮 AI Virtual Game Controller

An AI-powered Virtual Game Controller that uses **Computer Vision**, **MediaPipe Hands**, and **OpenCV** to control **Temple Run** using real-time hand movements instead of a physical keyboard or controller.

---

## 📌 Project Overview

The AI Virtual Game Controller detects a user's hand using a webcam and tracks its movement in real time. Instead of recognizing static gestures, the system calculates the movement of the hand's center and converts it into game actions such as moving left, moving right, jumping, sliding, and pausing.

The detected motions are translated into keyboard events that control Temple Run running inside an Android emulator such as BlueStacks.

---

## ✨ Features

- 🎥 Real-time webcam-based hand tracking
- ✋ MediaPipe 21-hand landmark detection
- 🎯 Motion-based gesture recognition
- 🎮 Temple Run game integration
- ⌨️ Keyboard automation
- 📊 Live FPS counter
- 📦 Modular project architecture
- 🖥️ Interactive OpenCV dashboard

---

## 🎮 Supported Game

- Temple Run
- Temple Run 2 (Android Emulator)

---

## 🛠️ Technologies Used

- Python 3.12
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- Pynput
- Android Emulator (BlueStacks)

---

## 📁 Project Structure

```
Virtual-Game-Controller
│
├── src
│   ├── controllers
│   │   ├── click_controller.py
│   │   ├── game_controller.py
│   │   ├── keyboard_controller.py
│   │   └── mouse_controller.py
│   │
│   ├── detectors
│   │   ├── gesture_detector.py
│   │   └── hand_detector.py
│   │
│   ├── config.py
│   ├── logger.py
│   ├── main.py
│   └── ui.py
│
├── logs
├── README.md
├── ABOUT.md
├── requirements.txt
└── LICENSE
```

---

## 🖥️ Installation

Clone the repository:

```bash
git clone https://github.com/purva008/Virtual-Game-Controller.git

cd Virtual-Game-Controller
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Navigate to the source folder:

```bash
cd src
```

Run:

```bash
python main.py
```

---

## 🎮 Temple Run Controls

| Hand Motion | Game Action |
|-------------|-------------|
| Move Left | Move Left |
| Move Right | Move Right |
| Move Up | Jump |
| Move Down | Slide |
| Open Palm | Pause |

---

## ⚙️ Workflow

```
Webcam
   │
   ▼
MediaPipe Hand Detection
   │
   ▼
Hand Landmark Extraction
   │
   ▼
Hand Center Calculation
   │
   ▼
Motion Detection
   │
   ▼
Game Controller
   │
   ▼
Keyboard Controller
   │
   ▼
Temple Run
```

---

## 📊 Advantages

- Contactless game control
- Real-time response
- No external sensors required
- Low hardware requirements
- Easy to extend for other games

---

## 🚀 Future Enhancements

- Multi-game support
- Custom gesture mapping
- Voice commands
- Two-hand interaction
- AI-based gesture classification
- User calibration mode

---

## 👨‍💻 Author

**Uttam Ahire**

AI Virtual Game Controller using Computer Vision and MediaPipe.

---

## 📜 License

This project is licensed under the MIT License.