"""
=========================================================
AI Virtual Game Controller
Camera Health Checker
=========================================================

Performs a complete health check of the webcam before
the application starts.

Features
--------
✓ Detect camera connection
✓ Configure camera resolution
✓ Capture test frame
✓ Read camera resolution
✓ Read camera FPS
✓ Return complete camera information
✓ Safe resource cleanup

Author : Uttam Ahire
Version : 3.0
=========================================================
"""

import cv2

from config import (
    CAMERA_INDEX,
    CAMERA_WIDTH,
    CAMERA_HEIGHT
)


class CameraChecker:
    """
    Camera Health Checker
    """

    def __init__(self):

        self.cap = None

        self.camera_info = {

            "connected": False,

            "frame_received": False,

            "width": 0,

            "height": 0,

            "fps": 0,

            "status": "NOT_INITIALIZED",

            "message": ""

        }

    # =====================================================
    # Connect Camera
    # =====================================================

    def connect(self):

        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        if not self.cap.isOpened():

            self.camera_info["status"] = "FAILED"

            self.camera_info["message"] = "Unable to access webcam."

            return False

        self.camera_info["connected"] = True

        return True

    # =====================================================
    # Configure Camera
    # =====================================================

    def configure(self):

        if self.cap is None:

            return

        self.cap.set(

            cv2.CAP_PROP_FRAME_WIDTH,

            CAMERA_WIDTH

        )

        self.cap.set(

            cv2.CAP_PROP_FRAME_HEIGHT,

            CAMERA_HEIGHT

        )

    # =====================================================
    # Capture Test
    # =====================================================

    def capture_test(self):

        if self.cap is None:

            return False

        success, frame = self.cap.read()

        if not success or frame is None:

            self.camera_info["frame_received"] = False

            self.camera_info["status"] = "FAILED"

            self.camera_info["message"] = "Unable to capture camera frame."

            return False

        self.camera_info["frame_received"] = True

        return True

    # =====================================================
    # Read Camera Information
    # =====================================================

    def read_information(self):

        if self.cap is None:

            return

        width = int(

            self.cap.get(

                cv2.CAP_PROP_FRAME_WIDTH

            )

        )

        height = int(

            self.cap.get(

                cv2.CAP_PROP_FRAME_HEIGHT

            )

        )

        fps = self.cap.get(

            cv2.CAP_PROP_FPS

        )

        if fps <= 1:

            fps = 30

        self.camera_info["width"] = width

        self.camera_info["height"] = height

        self.camera_info["fps"] = round(fps)

        self.camera_info["status"] = "READY"

        self.camera_info["message"] = "Camera is working properly."

    # =====================================================
    # Complete Camera Health Check
    # =====================================================

    def check(self):

        # Step 1
        if not self.connect():

            return self.camera_info

        # Step 2
        self.configure()

        # Step 3
        if not self.capture_test():

            return self.camera_info

        # Step 4
        self.read_information()

        return self.camera_info

    # =====================================================
    # Release Camera
    # =====================================================

    def release(self):

        if self.cap is not None:

            self.cap.release()

    # =====================================================
    # Print Camera Information
    # =====================================================

    def print_report(self):

        print("\n")

        print("=" * 55)

        print("Camera Health Report")

        print("=" * 55)

        print(

            f"Connected      : {self.camera_info['connected']}"

        )

        print(

            f"Frame Test     : {self.camera_info['frame_received']}"

        )

        print(

            f"Resolution     : "

            f"{self.camera_info['width']} x "

            f"{self.camera_info['height']}"

        )

        print(

            f"Camera FPS     : "

            f"{self.camera_info['fps']}"

        )

        print(

            f"Status         : "

            f"{self.camera_info['status']}"

        )

        print(

            f"Message        : "

            f"{self.camera_info['message']}"

        )

        print("=" * 55)

    # =====================================================
    # Standalone Test
    # =====================================================


if __name__ == "__main__":

    checker = CameraChecker()

    info = checker.check()

    checker.print_report()

    checker.release()