"""
=========================================================
AI Virtual Game Controller
Loading Manager
=========================================================

Handles the initialization of all application modules
before the main application starts.

Responsibilities
----------------
✓ Camera Initialization
✓ Hand Detector Initialization
✓ Gesture Detector Initialization
✓ Game Controller Initialization
✓ Progress Updates
✓ Error Handling
✓ Returns all initialized modules

Author : Uttam Ahire
Version : 2.0
=========================================================
"""

import time
import cv2

from config import (
    CAMERA_INDEX,
    CAMERA_WIDTH,
    CAMERA_HEIGHT
)

from detectors.hand_detector import HandDetector
from detectors.gesture_detector import GestureDetector
from controllers.game_controller import GameController
from system.camera_checker import CameraChecker
from system.system_info import SystemInfo
from system.performance_monitor import PerformanceMonitor
from system.camera_recovery import CameraRecovery
from logger.logger import Logger



class LoadingManager:
    """
    Professional Loading Manager
    """

    def __init__(self, splash=None):

        self.splash = splash

        self.modules = {}

        self.logger = Logger()

        self.logger.info("Loading Manager Initialized.")

        self.loading_steps = [

            ("Checking Camera Health...", self.check_camera),

            ("Opening Camera...", self.load_camera),

            ("Collecting System Information...", self.load_system_info),

            ("Loading MediaPipe...", self.load_hand_detector),

            ("Loading Gesture Engine...", self.load_gesture_detector),

            ("Loading Game Controller...", self.load_game_controller),

            ("Loading Camera Recovery...", self.load_camera_recovery),

            ("Preparing Dashboard...", self.load_dashboard),

            ("Finalizing Application...", self.finish_loading)

        ]

    # =====================================================
    # Update Splash
    # =====================================================

    def update(self, message, progress):

        print(message)

        if self.splash is not None:

            try:

                self.splash.update_progress(
                    progress,
                    message
                )

            except AttributeError:
                pass

        time.sleep(0.25)

    # =====================================================
    # Camera
    # =====================================================

    def check_camera(self):

        checker = CameraChecker()

        info = checker.check()

        checker.print_report()

        self.logger.system("Camera Health Check Completed.")

        if not info["connected"]:

            self.logger.error("No webcam detected.")

            raise RuntimeError(
                "No webcam detected."
            )

        if not info["frame_received"]:

            self.logger.error(
                "Unable to receive frames from the camera."
            )

            raise RuntimeError(
                "Unable to receive frames from the camera."
            )

        checker.release()

    def load_camera(self):

        cap = cv2.VideoCapture(CAMERA_INDEX)

        cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            CAMERA_WIDTH
        )

        cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            CAMERA_HEIGHT
        )

        if not cap.isOpened():

            raise RuntimeError(
                "Unable to access webcam."
            )

        self.modules["camera"] = cap

        self.logger.success("Camera Initialized Successfully.")

    def load_system_info(self):
        system = SystemInfo()
        info = system.get_info()
        system.print_report()
        self.modules["system_info"] = info
        self.logger.success("System Information Collected Successfully.")

    # =====================================================
    # Hand Detector
    # =====================================================

    def load_hand_detector(self):

        detector = HandDetector()

        self.modules["detector"] = detector

        self.logger.success("hand detector loaded successfully.")

    # =====================================================
    # Gesture Detector
    # =====================================================

    def load_gesture_detector(self):

        gesture = GestureDetector()

        self.modules["gesture_detector"] = gesture

        self.logger.success("Gesture detector loaded successfully.")

    # =====================================================
    # Game Controller
    # =====================================================

    def load_game_controller(self):

        controller = GameController()

        self.modules["game_controller"] = controller

        self.logger.success("Game controller loaded successfully.")

    # =====================================================
    # Dashboard
    # =====================================================

    def load_dashboard(self):

        performance = PerformanceMonitor()

        self.modules["performance"] = performance
        self.logger.success("Performance monitor initialized successfully.")

        time.sleep(0.3)

        self.modules["dashboard_ready"] = True
        self.logger.info("Dashboard Ready")
    # =====================================================
    # Camera Recovery
    # =====================================================

    def load_camera_recovery(self):
        if "camera" not in self.modules:

            raise RuntimeError(

                "Camera must be initialized before Camera Recovery."

            )

        recovery = CameraRecovery()

        recovery.attach_camera(

            self.modules["camera"]

        )

    self.modules["camera_recovery"] = recovery

    self.logger.success(

        "Camera Recovery Engine Loaded"

    )

    # =====================================================
    # Finish
    # =====================================================

    def finish_loading(self):

        time.sleep(0.2)

        self.modules["ready"] = True
        self.logger.info("Application Ready")

    # =====================================================
    # Initialize Everything
    # =====================================================

    def initialize(self):

        total = len(self.loading_steps)

        for index, (message, function) in enumerate(
            self.loading_steps,
            start=1
        ):

            progress = int((index / total) * 100)

            self.update(
                message,
                progress
            )

            function()

        self.modules["logger"] = self.logger
        return self.modules

    # =====================================================
    # Cleanup
    # =====================================================

    def release(self):
        if "camera_recovery" in self.modules:

            self.modules["camera_recovery"].release_camera()

        if "camera" in self.modules:

            self.modules["camera"].release()

        if "detector" in self.modules:

            self.modules["detector"].close()
        
        if hasattr(self, "logger"):
            self.logger.close()