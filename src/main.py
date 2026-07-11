import cv2
import time

from detectors.hand_detector import HandDetector
from controllers.mouse_controller import move_mouse
from controllers.click_controller import (
    left_click,
    right_click,
    start_drag,
    stop_drag,
)
from controllers.scroll_controller import scroll_up, scroll_down
from ui import draw_dashboard
from utils.fps import FPSCounter
from utils.gesture_stabilizer import GestureStabilizer
from config import CAMERA_INDEX, CLICK_DELAY, GESTURE_STABILITY
from utils.logger import logger

# Open Camera
camera = cv2.VideoCapture(CAMERA_INDEX)
logger.info("Application Started")

# Initialize Objects
detector = HandDetector()
fps_counter = FPSCounter()
stabilizer = GestureStabilizer(delay=GESTURE_STABILITY)

last_click_time = 0
click_delay = CLICK_DELAY
dragging = False

while True:

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    detector.detectHands(frame)
    landmarkList = detector.findPosition(frame)

    action = "None"
    hand_detected = False

    if len(landmarkList) != 0:

        hand_detected = True

        fingers = detector.fingersUp(landmarkList)
        total = fingers.count(1)

        stable = stabilizer.is_stable(total)

        if not stable:
            action = "Detecting..."

        else:

            cam_height, cam_width, _ = frame.shape

            index_x = landmarkList[8][1]
            index_y = landmarkList[8][2]

            # 1 Finger -> Move Mouse
            if total == 1:
                move_mouse(index_x, index_y, cam_width, cam_height)
                action = "Move Mouse"

            # 2 Fingers -> Left Click
            elif total == 2:

                current_time = time.time()

                if current_time - last_click_time > click_delay:
                    left_click()
                    last_click_time = current_time

                action = "Left Click"

            # 3 Fingers -> Right Click
            elif total == 3:

                current_time = time.time()

                if current_time - last_click_time > click_delay:
                    right_click()
                    last_click_time = current_time

                action = "Right Click"

            # 4 Fingers -> Scroll
            elif total == 4:

                if index_y < cam_height // 2:
                    scroll_up()
                    action = "Scroll Up"
                else:
                    scroll_down()
                    action = "Scroll Down"

            # Closed Fist -> Drag
            elif total == 0:

                if not dragging:
                    start_drag()
                    dragging = True

                action = "Dragging"

            # Open Palm -> Release
            elif total == 5:

                if dragging:
                    stop_drag()
                    dragging = False

                action = "Release"

    # FPS & Session Time
    fps = fps_counter.get_fps()
    session_time = fps_counter.get_session_time()

    # Draw Dashboard
    frame = draw_dashboard(
        frame,
        fps,
        action,
        hand_detected,
        session_time,
    )

    cv2.imshow("Virtual Game Controller", frame)

    # Keyboard Shortcuts
    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord("q"):
        break

    # Save Screenshot
    elif key == ord("s"):
        filename = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved: {filename}")

    # Reset Drag State
    elif key == ord("r"):
        dragging = False
        print("Gesture state reset.")


logger.info("Application Closed")
camera.release()
cv2.destroyAllWindows()