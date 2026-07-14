"""
=========================================================
AI Virtual Game Controller
Main Application
=========================================================
Uses webcam input to control Temple Run
through real-time hand motion.
=========================================================
"""

import cv2
import time

from config import (
    CAMERA_INDEX,
    CAMERA_WIDTH,
    CAMERA_HEIGHT,
    WINDOW_NAME
)

from detectors.hand_detector import HandDetector
from detectors.gesture_detector import GestureDetector
from controllers.game_controller import GameController
from ui import draw_ui


# =========================================================
# Initialize Modules
# =========================================================

detector = HandDetector()
gesture_detector = GestureDetector()
game_controller = GameController()


# =========================================================
# Initialize Camera
# =========================================================

cap = cv2.VideoCapture(CAMERA_INDEX)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

if not cap.isOpened():
    print("ERROR: Unable to access webcam.")
    exit()

print("=" * 55)
print("        AI Virtual Game Controller")
print("        Motion-Based Temple Run Controller")
print("=" * 55)
print("Controls:")
print("Move Hand Left   -> LEFT")
print("Move Hand Right  -> RIGHT")
print("Move Hand Up     -> JUMP")
print("Move Hand Down   -> SLIDE")
print("Open Palm        -> PAUSE")
print("Press Q to Exit")
print("=" * 55)


# =========================================================
# FPS
# =========================================================

previous_time = 0


# =========================================================
# Main Loop
# =========================================================

display_action = "NONE"
while True:

    success, frame = cap.read()

    if not success:
        print("Camera frame not received.")
        break

    # Mirror the camera
    frame = cv2.flip(frame, 1)

    # -----------------------------------------------------
    # Detect Hand
    # -----------------------------------------------------

    frame = detector.find_hands(frame)

    (
        landmarks,
        landmark_dict,
        hand_type,
        bbox,
        hand_center
    ) = detector.get_landmarks(frame)

    # -----------------------------------------------------
    # Detect Motion
    # -----------------------------------------------------

    action = gesture_detector.recognize(
        hand_center,
        landmark_dict,
        hand_type
    )

    game_controller.execute(action)
    # -----------------------------------------------------
    # Execute Game Action
    # -----------------------------------------------------

    if action != "NONE":
        display_action = action
        game_controller.execute(action)

    # -----------------------------------------------------
    # FPS Calculation
    # -----------------------------------------------------

    current_time = time.time()

    if previous_time == 0:
        fps = 0
    else:
        fps = int(1 / (current_time - previous_time))

    previous_time = current_time

    # -----------------------------------------------------
    # Draw Hand Center
    # -----------------------------------------------------

    if hand_center is not None:

        cv2.circle(
            frame,
            hand_center,
            8,
            (0, 0, 255),
            -1
        )

        cv2.putText(
            frame,
            "CENTER",
            (hand_center[0] + 10, hand_center[1]),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    # -----------------------------------------------------
    # Draw UI
    # -----------------------------------------------------

    frame = draw_ui(
        frame=frame,
        gesture=action,
        hand_type=hand_type,
        fps=fps,
        bbox=bbox
    )

    # -----------------------------------------------------
    # Show Window
    # -----------------------------------------------------

    cv2.imshow(
        WINDOW_NAME,
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


# =========================================================
# Cleanup
# =========================================================

cap.release()

detector.close()

cv2.destroyAllWindows()

print("\nApplication Closed Successfully.")