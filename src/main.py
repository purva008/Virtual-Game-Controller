import cv2
import time

from hand_detector import HandDetector
from automation import move_left, move_right, jump, attack, pause_game
from mouse_controller import (
    move_mouse,
    left_click,
    right_click,
    start_drag,
    stop_drag,
    reset_click,
)
from fps import FPS

camera = cv2.VideoCapture(0)

detector = HandDetector()
fps_counter = FPS()

last_action_time = 0
action_delay = 1

while True:

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    detector.detectHands(frame)

    landmarkList = detector.findPosition(frame)

    action = "None"
    status = "No Hand"
    mode = "Mouse + Game"

    if len(landmarkList) != 0:

        status = "Hand Detected"

        # Mouse Movement
        x = landmarkList[8][1]
        y = landmarkList[8][2]

        h, w, _ = frame.shape

        move_mouse(x, y, w, h)

        fingers = detector.fingersUp(landmarkList)
        total = fingers.count(1)

        # Mouse Gestures
        if fingers == [0, 1, 1, 0, 0]:
            left_click()
            stop_drag()
            action = "Left Click"

        elif fingers == [0, 1, 1, 1, 0]:
            right_click()
            stop_drag()
            action = "Right Click"

        elif fingers == [0, 1, 1, 1, 1]:
            start_drag()
            action = "Dragging"

        else:
            stop_drag()
            reset_click()

        # Game Gestures
        current_time = time.time()

        if current_time - last_action_time > action_delay:

            if total == 1:
                move_left()
                action = "Move Left"

            elif total == 2:
                move_right()
                action = "Move Right"

            elif total == 3:
                jump()
                action = "Jump"

            elif total == 0:
                attack()
                action = "Attack"

            elif total == 5:
                pause_game()
                action = "Pause"

            last_action_time = current_time

    fps = fps_counter.get_fps()

    # Dashboard Background
    cv2.rectangle(frame, (10, 10), (340, 160), (40, 40, 40), -1)

    cv2.putText(
        frame,
        "Virtual Game Controller",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2,
    )

    cv2.putText(
        frame,
        f"FPS : {fps}",
        (20, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        frame,
        f"Gesture : {action}",
        (20, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Mode : {mode}",
        (20, 125),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Status : {status}",
        (20, 155),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2,
    )

    cv2.imshow("Virtual Game Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()