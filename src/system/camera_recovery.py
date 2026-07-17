"""
=========================================================
AI Virtual Game Controller
Professional Camera Recovery Engine
=========================================================

Responsibilities

✓ Detect Camera Failure
✓ Automatic Camera Recovery
✓ Retry Management
✓ Recovery Statistics
✓ Camera State Management

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
# =========================================================
# Camera States
# =========================================================

CAMERA_CONNECTED = "CONNECTED"

CAMERA_FRAME_LOST = "FRAME_LOST"

CAMERA_RECOVERING = "RECOVERING"

CAMERA_FAILED = "FAILED"
# =========================================================
# Camera Recovery
# =========================================================

class CameraRecovery:
    """
    Professional Camera Recovery System.
    """

    def __init__(self):
                # ----------------------------------------------
        # Camera Object
        # ----------------------------------------------

        self.camera = None

        # ----------------------------------------------
        # Current Camera State
        # ----------------------------------------------

        self.state = CAMERA_CONNECTED

        # ----------------------------------------------
        # Retry Information
        # ----------------------------------------------

        self.retry_count = 0

        self.max_retries = 5

        self.retry_interval = 2.0

        self.last_retry_time = 0

        # ----------------------------------------------
        # Statistics
        # ----------------------------------------------

        self.total_failures = 0

        self.total_recoveries = 0

        # ----------------------------------------------
        # Runtime
        # ----------------------------------------------

        self.last_frame_time = time.time()

        self.frame_timeout = 3.0

        # ----------------------------------------------
        # Status Message
        # ----------------------------------------------

        self.status_message = "Camera Connected"
    # =====================================================
    # Current State
    # =====================================================

    def get_state(self):

        return self.state
    # =====================================================
    # Status Message
    # =====================================================

    def get_status(self):

        return self.status_message
    
    # =====================================================
    # Attach Camera
    # =====================================================

    def attach_camera(self, camera):

        self.camera = camera

        self.state = CAMERA_CONNECTED

        self.status_message = "Camera Connected"
    # =====================================================
    # Reset Recovery
    # =====================================================

    def reset(self):

        self.retry_count = 0

        self.state = CAMERA_CONNECTED

        self.status_message = "Camera Connected"
    # =====================================================
    # Update Frame Timer
    # =====================================================

    def update_frame_timestamp(self):
        """
        Call this whenever a valid frame is received.
        """

        self.last_frame_time = time.time()

        if self.state != CAMERA_CONNECTED:

            self.state = CAMERA_CONNECTED

            self.status_message = "Camera Connected"

            self.retry_count = 0
    # =====================================================
    # Detect Frame Timeout
    # =====================================================

    def detect_frame_loss(self):
        """
        Detect if the camera has stopped providing frames.
        """

        elapsed = time.time() - self.last_frame_time

        if elapsed > self.frame_timeout:

            self.state = CAMERA_FRAME_LOST

            self.status_message = "Frame Timeout"

            self.total_failures += 1

            return True

        return False
    # =====================================================
    # Detect Camera Disconnect
    # =====================================================

    def detect_camera_disconnect(self):
        """
        Check whether the camera object is still valid.
        """

        if self.camera is None:

            self.state = CAMERA_FAILED

            self.status_message = "Camera Not Attached"

            return True

        if not self.camera.isOpened():

            self.state = CAMERA_FAILED

            self.status_message = "Camera Disconnected"

            self.total_failures += 1

            return True

        return False
    # =====================================================
    # Camera Health Check
    # =====================================================

    def check_camera(self):
        """
        Performs a complete camera health check.

        Returns
        -------
        bool
            True  -> Camera healthy
            False -> Recovery required
        """

        if self.detect_camera_disconnect():

            return False

        if self.detect_frame_loss():

            return False

        return True
    # =====================================================
    # Prepare Recovery
    # =====================================================

    def prepare_recovery(self):
        """
        Move recovery system into RECOVERING state.
        """

        self.state = CAMERA_RECOVERING

        self.status_message = "Recovering Camera..."

        self.last_retry_time = time.time()
    # =====================================================
    # Recovery Needed
    # =====================================================

    def recovery_required(self):
        """
        Returns True if camera recovery should start.
        """

        return self.state in (

            CAMERA_FAILED,

            CAMERA_FRAME_LOST

        )
    # =====================================================
    # Retry Timer
    # =====================================================

    def can_retry(self):
        """
        Returns True if enough time has passed
        to attempt another camera recovery.
        """

        current_time = time.time()

        return (
            current_time - self.last_retry_time
        ) >= self.retry_interval
    # =====================================================
    # Safe Camera Release
    # =====================================================

    def release_camera(self):
        """
        Safely releases the current camera.
        """

        try:

            if self.camera is not None:

                self.camera.release()

        except Exception:

            pass

        self.camera = None
    # =====================================================
    # Reconnect Camera
    # =====================================================

    def reconnect(self):
        """
        Attempts to reconnect to the webcam.

        Returns
        -------
        bool
            True if recovery succeeded.
        """

        if self.retry_count >= self.max_retries:

            self.state = CAMERA_FAILED

            self.status_message = "Maximum retries reached."

            return False

        if not self.can_retry():

            return False

        self.last_retry_time = time.time()

        self.retry_count += 1

        self.release_camera()

        try:

            camera = cv2.VideoCapture(CAMERA_INDEX)

            camera.set(
                cv2.CAP_PROP_FRAME_WIDTH,
                CAMERA_WIDTH
            )

            camera.set(
                cv2.CAP_PROP_FRAME_HEIGHT,
                CAMERA_HEIGHT
            )

            if not camera.isOpened():

                self.status_message = (
                    f"Retry {self.retry_count} failed."
                )

                return False

            self.camera = camera

            self.state = CAMERA_CONNECTED

            self.status_message = (
                "Camera Reconnected Successfully"
            )

            self.retry_count = 0

            self.total_recoveries += 1

            self.last_frame_time = time.time()

            return True

        except Exception:

            self.status_message = (
                f"Retry {self.retry_count} failed."
            )

            return False
    # =====================================================
    # Automatic Recovery
    # =====================================================

    def recover(self):
        """
        Executes one recovery cycle.

        Returns
        -------
        bool
            True if camera is recovered.
        """

        if not self.recovery_required():

            return True

        self.prepare_recovery()

        return self.reconnect()
    # =====================================================
    # Camera Getter
    # =====================================================

    def get_camera(self):
        """
        Returns the active camera object.
        """

        return self.camera
    # =====================================================
    # Current Status
    # =====================================================

    def get_status_message(self):

        return self.status_message
    # =====================================================
    # Camera Connected
    # =====================================================

    def is_connected(self):

        return self.state == CAMERA_CONNECTED
    # =====================================================
    # Recovery Success Rate
    # =====================================================

    def get_success_rate(self):
        """
        Returns camera recovery success rate.
        """

        if self.total_failures == 0:

            return 100.0

        return (
            self.total_recoveries /
            self.total_failures
        ) * 100
    # =====================================================
    # Recovery Statistics
    # =====================================================

    def get_statistics(self):

        return {

            "state": self.state,

            "status": self.status_message,

            "retry_count": self.retry_count,

            "total_failures": self.total_failures,

            "total_recoveries": self.total_recoveries,

            "success_rate": self.get_success_rate(),

            "frame_timeout": self.frame_timeout,

            "max_retries": self.max_retries

        }
    # =====================================================
    # Recovery Summary
    # =====================================================

    def print_summary(self):

        print()

        print("=" * 60)

        print("Camera Recovery Summary")

        print("=" * 60)

        print(f"State              : {self.state}")

        print(f"Status             : {self.status_message}")

        print(f"Failures           : {self.total_failures}")

        print(f"Recoveries         : {self.total_recoveries}")

        print(
            f"Recovery Rate      : "
            f"{self.get_success_rate():.1f}%"
        )

        print(f"Retry Count        : {self.retry_count}")

        print("=" * 60)
    # =====================================================
    # Force Failure (Debug)
    # =====================================================

    def simulate_failure(self):

        self.state = CAMERA_FAILED

        self.status_message = "Simulated Failure"

        self.total_failures += 1
# =========================================================
# Standalone Testing
# =========================================================

if __name__ == "__main__":

    recovery = CameraRecovery()

    recovery.simulate_failure()

    print(recovery.get_statistics())

    recovery.print_summary()