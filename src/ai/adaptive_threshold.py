"""
=========================================================
Adaptive Threshold Engine
AI Virtual Game Controller
=========================================================

Learns user movement speed and automatically
adjusts motion detection thresholds.

Author : AI Virtual Game Controller
=========================================================
"""

from collections import deque

import time


class AdaptiveThreshold:
    """
    Adaptive motion threshold engine.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(

        self,

        default_x=35,

        default_y=30,

        history_size=60

    ):

        # ---------------------------------------------
        # Default Thresholds
        # ---------------------------------------------

        self.default_x = default_x
        self.default_y = default_y

        # Current adaptive thresholds

        self.current_x = default_x
        self.current_y = default_y

        # ---------------------------------------------
        # Motion History
        # ---------------------------------------------

        self.motion_x = deque(maxlen=history_size)

        self.motion_y = deque(maxlen=history_size)

        # ---------------------------------------------
        # Calibration
        # ---------------------------------------------

        self.calibrated = False

        self.calibration_start = time.time()

        self.calibration_duration = 5.0

        # ---------------------------------------------
        # Statistics
        # ---------------------------------------------

        self.total_updates = 0

        self.average_motion = 0.0

        self.maximum_motion = 0.0

        self.minimum_motion = float("inf")
    # =====================================================
    # Update Motion
    # =====================================================

    def update(

        self,

        dx,

        dy

    ):
        """
        Update motion history.
        """

        dx = abs(float(dx))
        dy = abs(float(dy))

        self.motion_x.append(dx)
        self.motion_y.append(dy)

        self.total_updates += 1

        magnitude = (dx + dy) / 2.0

        self.maximum_motion = max(

            self.maximum_motion,

            magnitude

        )

        self.minimum_motion = min(

            self.minimum_motion,

            magnitude

        )

        self._recalculate_thresholds()
    # =====================================================
    # Recalculate Thresholds
    # =====================================================

    def _recalculate_thresholds(

        self

    ):
        """
        Dynamically calculate thresholds.
        """

        if len(self.motion_x) < 10:

            return

        avg_x = sum(self.motion_x) / len(self.motion_x)

        avg_y = sum(self.motion_y) / len(self.motion_y)

        self.average_motion = (

            avg_x + avg_y

        ) / 2.0

        # -------------------------------------------------
        # Adaptive Scaling
        # -------------------------------------------------

        scale = max(

            0.7,

            min(

                1.6,

                self.average_motion / 25.0

            )

        )

        self.current_x = int(

            self.default_x * scale

        )

        self.current_y = int(

            self.default_y * scale

        )
    # =====================================================
    # Calibration Status
    # =====================================================

    def is_calibrated(

        self

    ):
        """
        Check calibration state.
        """

        if self.calibrated:

            return True

        elapsed = (

            time.time()

            -

            self.calibration_start

        )

        if elapsed >= self.calibration_duration:

            self.calibrated = True

        return self.calibrated
    # =====================================================
    # Get X Threshold
    # =====================================================

    def get_threshold_x(self):
        """
        Return current adaptive X threshold.
        """

        return self.current_x
    # =====================================================
    # Get Y Threshold
    # =====================================================

    def get_threshold_y(self):
        """
        Return current adaptive Y threshold.
        """

        return self.current_y
    # =====================================================
    # Statistics
    # =====================================================

    def get_statistics(self):
        """
        Return threshold statistics.
        """

        minimum = 0.0

        if self.minimum_motion != float("inf"):

            minimum = self.minimum_motion

        return {

            "current_x": self.current_x,

            "current_y": self.current_y,

            "average_motion": round(

                self.average_motion,

                2

            ),

            "maximum_motion": round(

                self.maximum_motion,

                2

            ),

            "minimum_motion": round(

                minimum,

                2

            ),

            "total_updates": self.total_updates,

            "calibrated": self.calibrated

        }
    # =====================================================
    # Reset
    # =====================================================

    def reset(self):
        """
        Reset adaptive engine.
        """

        self.motion_x.clear()

        self.motion_y.clear()

        self.current_x = self.default_x

        self.current_y = self.default_y

        self.total_updates = 0

        self.average_motion = 0.0

        self.maximum_motion = 0.0

        self.minimum_motion = float("inf")

        self.calibrated = False

        self.calibration_start = time.time()
    # =====================================================
    # String Representation
    # =====================================================

    def __str__(self):

        return (

            f"AdaptiveThreshold("

            f"X={self.current_x}, "

            f"Y={self.current_y}, "

            f"AvgMotion={self.average_motion:.2f}, "

            f"Updates={self.total_updates})"

        )
                                        
