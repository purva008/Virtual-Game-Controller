# About the Project

## AI Virtual Game Controller

The AI Virtual Game Controller is a Computer Vision project developed in Python that enables users to control the popular mobile game Temple Run using natural hand movements captured through a webcam.

Unlike traditional systems that rely on static hand gestures, this project uses motion-based interaction. The application continuously tracks the center of the detected hand and determines its movement direction to trigger corresponding game actions.

The project demonstrates the practical application of Artificial Intelligence, Computer Vision, Human-Computer Interaction, and Automation.

---

## Objective

The objective of this project is to provide a touch-free gaming experience by replacing conventional keyboard input with intuitive hand movements.

---

## Working Principle

1. Capture live video using a webcam.
2. Detect the user's hand using MediaPipe Hands.
3. Extract all 21 hand landmarks.
4. Calculate the center of the hand.
5. Track movement between frames.
6. Recognize movement direction.
7. Convert movements into keyboard events.
8. Control Temple Run in real time.

---

## Motion Mapping

| Hand Motion | Action |
|-------------|--------|
| Left | Move Left |
| Right | Move Right |
| Up | Jump |
| Down | Slide |
| Open Palm | Pause |

---

## Technologies

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- Pynput

---

## Applications

- Gesture-controlled gaming
- Human-Computer Interaction
- Touchless interfaces
- Computer Vision research
- AI-based automation
- Educational demonstrations

---

## Advantages

- Real-time performance
- Easy to use
- No specialized hardware
- Cost-effective
- Highly modular
- Expandable to multiple games

---

## Future Scope

The project can be enhanced by adding:

- Machine Learning gesture classification
- Dynamic gesture recording
- Support for multiple games
- VR integration
- Hand tracking using depth cameras
- Voice command support
- User-specific calibration
- Wireless control

---

## Conclusion

The AI Virtual Game Controller successfully demonstrates how Computer Vision and Artificial Intelligence can create an intuitive and interactive gaming experience. By integrating MediaPipe hand tracking with keyboard automation, the system allows users to play Temple Run using natural hand movements, offering a practical example of modern Human-Computer Interaction.

# Admin/ Developed by : Purva Ahire