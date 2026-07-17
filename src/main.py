"""
=========================================================
AI Virtual Game Controller
Main Application
=========================================================

This is the central application that integrates:

✓ Camera Manager
✓ Hand Tracker
✓ Gesture Detector
✓ AI Core
✓ Game Controller
✓ Professional UI
✓ Logger
✓ Motion Trail
✓ System Monitor
✓ Camera Recovery
✓ Performance Statistics

Author : Uttam Ahire
Version : 4.0
=========================================================
"""

import cv2
import time
from collections import deque

# ==========================================================
# Configuration
# ==========================================================

from config import *

# ==========================================================
# Detection
# ==========================================================

from detectors.hand_detector import HandDetector
from detectors.gesture_detector import GestureDetector

# ==========================================================
# Controllers
# ==========================================================

from controllers.game_controller import GameController

# ==========================================================
# Monitoring
# ==========================================================

from system.performance_monitor import PerformanceMonitor
from system.system_info import SystemInfo
from system.camera_recovery import CameraRecovery

# ==========================================================
# User Interface
# ==========================================================

from ui.ui import draw_ui


def main():

    print("=" * 60)
    print("AI Virtual Game Controller")
    print("=" * 60)

    camera = cv2.VideoCapture(CAMERA_INDEX)

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

    if not camera.isOpened():
        print("Camera Error")
        return

    camera_recovery = CameraRecovery()
    camera_recovery.attach_camera(camera)

    performance = PerformanceMonitor()

    system_info = SystemInfo()

    hand_detector = HandDetector()

    gesture_detector = GestureDetector()

    game_controller = GameController()

    # =====================================================
    # Runtime Variables
    # =====================================================

    motion_trail = deque(maxlen=25)

    running = True

    while running:

        # ---------------------------------------------
        # Performance Update
        # ---------------------------------------------

        performance.update()

        stats = performance.get_stats()

        fps = stats["fps"]
        average_fps = stats["average_fps"]
        runtime = stats["runtime"]

        # ---------------------------------------------
        # Camera Recovery Check
        # ---------------------------------------------

        if not camera_recovery.check_camera():

            print("[Camera] Recovery Started...")

            if camera_recovery.recover():

                camera = camera_recovery.get_camera()

            else:

                continue

        # ---------------------------------------------
        # Capture Frame
        # ---------------------------------------------

        success, frame = camera.read()

        if not success:

            continue

        camera_recovery.update_frame_timestamp()

        # Mirror image
        frame = cv2.flip(frame, 1)

        # ---------------------------------------------
        # Hand Detection
        # ---------------------------------------------

        frame = hand_detector.find_hands(frame)

        (
            landmarks,
            landmark_dict,
            hand_type,
            bbox,
            hand_center

        ) = hand_detector.get_landmarks(frame)

        # ---------------------------------------------
        # Motion Trail
        # ---------------------------------------------

        if hand_center is not None:

            motion_trail.append(hand_center)

        # ---------------------------------------------
        # Gesture Recognition
        # ---------------------------------------------

        gesture = gesture_detector.recognize(

            hand_center,

            landmark_dict,

            hand_type

        )

        # ---------------------------------------------
        # Execute Game Action
        # ---------------------------------------------

        game_controller.execute(gesture)

        # ---------------------------------------------
        # System Information
        # ---------------------------------------------

        system = system_info.get_info()

        # ---------------------------------------------
        # Camera Statistics
        # ---------------------------------------------

        camera_stats = camera_recovery.get_statistics()

        # ---------------------------------------------
        # Draw Professional Dashboard
        # ---------------------------------------------

        frame = draw_ui(

            frame=frame,

            gesture=gesture,

            fps=fps,

            runtime=runtime,

            bbox=bbox,

            hand_center=hand_center,

            motion_trail=list(motion_trail),

            average_fps=average_fps,

            system_info=system,

            camera_stats=camera_stats

        )

        # ---------------------------------------------
        # Display
        # ---------------------------------------------

        cv2.imshow(

            WINDOW_NAME,

            frame

        )

        # ---------------------------------------------
        # Quit
        # ---------------------------------------------

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):

            running = False

    # =====================================================
    # Cleanup
    # =====================================================

    print()

    print("=" * 60)
    print("Shutting Down...")
    print("=" * 60)


    # ---------------------------------------------
    # Release Camera
    # ---------------------------------------------

    if camera is not None:

        camera.release()

    # ---------------------------------------------
    # Close MediaPipe
    # ---------------------------------------------

    hand_detector.close()

    # ---------------------------------------------
    # Destroy OpenCV Windows
    # ---------------------------------------------

    cv2.destroyAllWindows()

# =====================================================
# Entry Point
# =====================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print()

        print("Application Interrupted by User.")

    except Exception as e:

        print()

        print("=" * 60)
        print("Unexpected Error:")
        print(e)
        print("=" * 60)