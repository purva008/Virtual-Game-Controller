============================================================
                     ABOUT
============================================================


# AI Virtual Game Controller
### Intelligent Hand Gesture-Based Control System for Temple Run

---

## Project Overview

The **AI Virtual Game Controller** is a real-time Computer Vision and Artificial Intelligence application that enables users to control the **Temple Run** game entirely through natural hand gestures without using a keyboard or mouse.

The system captures live video from a webcam, detects and tracks the user's hand using **MediaPipe**, analyzes hand movement through an AI-powered gesture recognition pipeline, and converts recognized gestures into corresponding keyboard commands for seamless game interaction.

Designed with a modular software architecture, the project demonstrates the practical application of **Artificial Intelligence, Human-Computer Interaction (HCI), and Computer Vision** to create an intuitive, touch-free gaming experience.

---

# Problem Statement

Traditional computer games rely on physical input devices such as keyboards, mice, or controllers. These interaction methods limit accessibility and reduce the naturalness of user interaction.

This project addresses this limitation by providing an intelligent gesture-based control mechanism capable of replacing conventional input devices using real-time vision-based hand tracking.

---

# Objectives

The primary objectives of this project are:

- Develop a real-time hand gesture recognition system.
- Replace keyboard controls with natural hand movements.
- Integrate AI-based gesture processing for improved accuracy.
- Control Temple Run using contactless interaction.
- Demonstrate practical implementation of AI and Computer Vision techniques.

---

# System Architecture

```
                    Webcam
                       │
                       ▼
             Hand Detection (MediaPipe)
                       │
                       ▼
             Landmark Extraction (21 Points)
                       │
                       ▼
              Motion Vector Calculation
                       │
                       ▼
            Adaptive Threshold Engine
                       │
                       ▼
             Gesture Smoothing Module
                       │
                       ▼
                 AI Core Processing
                       │
                       ▼
           Temple Run Game Controller
                       │
                       ▼
              Real-Time Game Actions
```

---

# Core Features

## Real-Time Hand Detection

- High-speed hand tracking using MediaPipe Hands
- 21 landmark extraction
- Automatic hand center calculation
- Bounding box generation

---

## AI Gesture Recognition

Recognizes movement-based gestures including:

- Move Left
- Move Right
- Jump
- Slide
- Pause

---

## AI Core Engine

The AI Core coordinates multiple intelligent modules:

- Gesture Smoother
- Adaptive Threshold
- AI Statistics
- Confidence Tracking
- Processing Time Analysis

The architecture is designed to support future AI extensions such as gesture prediction and personalized learning.

---

## Adaptive Threshold Algorithm

Instead of relying on fixed movement thresholds, the system dynamically adjusts sensitivity according to the user's hand movement, improving recognition accuracy under varying conditions.

---

## Gesture Smoothing

A history-based majority voting algorithm filters noisy detections and minimizes false positives, resulting in stable and reliable gesture recognition.

---

## Game Integration

Recognized gestures are mapped directly to Temple Run controls using automated keyboard input.

This provides a smooth, real-time gaming experience without physical interaction.

---

## Performance Monitoring

The application continuously monitors:

- Frames Per Second (FPS)
- Frame Processing Time
- CPU Usage
- Memory Usage
- Application Runtime

---

## Camera Recovery

An automatic recovery engine detects camera interruptions and attempts reconnection without restarting the application.

---

# Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| Numerical Computing | NumPy |
| Automation | PyAutoGUI |
| System Monitoring | psutil |
| AI Backend | TensorFlow Lite (MediaPipe) |

---

# Software Engineering Practices

The project follows a modular software architecture to ensure maintainability, scalability, and readability.

Major modules include:

- AI Engine
- Gesture Recognition
- Controllers
- Camera Management
- Performance Monitoring
- System Information
- User Interface
- Logging

This structure allows future enhancements with minimal code modification.

---

# Applications

The techniques implemented in this project can be extended to:

- Gesture-Controlled Gaming
- Human–Computer Interaction (HCI)
- Smart Interactive Systems
- Touchless User Interfaces
- Accessibility Technologies
- Virtual Reality (VR)
- Augmented Reality (AR)
- Industrial Automation

---

# Future Enhancements

Potential improvements include:

- Deep Learning-based Gesture Classification
- Personalized Gesture Training
- AI Gesture Prediction
- Custom Gesture Creation
- Voice and Gesture Hybrid Control
- Multi-Hand Recognition
- Cloud-Based AI Analytics
- VR/AR Gesture Interaction

---

# Developer

**Purva Ahire**

Specialization:
- Artificial Intelligence
- Computer Vision
- Human–Computer Interaction

---

# Acknowledgement

This project was developed as part of the Final Year Engineering curriculum to demonstrate the practical implementation of Artificial Intelligence, Computer Vision, and Human–Computer Interaction in an interactive real-time gaming environment.

The project integrates modern vision-based technologies with intelligent software design principles to deliver an efficient, modular, and user-friendly gesture-controlled gaming system.

---

© 2026 Purva Ahire. All Rights Reserved.