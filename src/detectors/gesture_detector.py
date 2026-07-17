"""
=========================================================
AI Virtual Game Controller
Motion-Based Gesture Detector
=========================================================
Detects:

LEFT
RIGHT
JUMP
SLIDE
PAUSE

using hand movement instead of fixed gestures.
=========================================================
"""

import time

from config import (
    
    MOTION_COOLDOWN
)
from ai.ai_core import AICore

class GestureDetector:

    def __init__(self):

        # Previous hand center
        self.previous_center = None

        # Cooldown timer
        self.last_action_time = 0

        # Last detected action (used by UI)
        self.last_action = "NONE"
        
        # =====================================================
        # AI Core
        # =====================================================

        self.ai = AICore()
        # =====================================================
        # Statistics
        # =====================================================

        self.total_predictions = 0

        self.valid_predictions = 0

    # --------------------------------------------------
    # Open Palm Detection
    # --------------------------------------------------

    def is_open_palm(self, landmark_dict, hand_type):

        if len(landmark_dict) != 21:
            return False

        fingers = []

        # Thumb

        if hand_type == "Right":
            fingers.append(
                landmark_dict[4][0] > landmark_dict[3][0]
            )
        else:
            fingers.append(
                landmark_dict[4][0] < landmark_dict[3][0]
            )

        # Index, Middle, Ring, Pinky

        tip_ids = [8, 12, 16, 20]
        pip_ids = [6, 10, 14, 18]

        for tip, pip in zip(tip_ids, pip_ids):

            fingers.append(
                landmark_dict[tip][1] <
                landmark_dict[pip][1]
            )

        return all(fingers)

    # --------------------------------------------------
    # Motion Recognition
    # --------------------------------------------------

    def recognize(

    self,

    hand_center,

    landmark_dict,

    hand_type

    ):

        """
        Recognize gesture based on hand movement.
        """

        # Default value (prevents "stable" variable errors)
        stable = "NONE"

        # --------------------------------------------------
        # No Hand Detected
        # --------------------------------------------------

        if hand_center is None:

            self.previous_center = None

            self.last_action = "NONE"

            return "NONE"

    
        # --------------------------------------------------
        # First Frame
        # --------------------------------------------------

        if self.previous_center is None:

            self.previous_center = hand_center

            return "NONE"

        prev_x, prev_y = self.previous_center

        curr_x, curr_y = hand_center

        dx = curr_x - prev_x

        dy = curr_y - prev_y

        self.previous_center = hand_center

        current_time = time.time()

        # --------------------------------------------------
        # Cooldown
        # --------------------------------------------------

        if current_time - self.last_action_time < MOTION_COOLDOWN:

            return self.ai.get_gesture()

        # --------------------------------------------------
        # Pause (Open Palm)
        # --------------------------------------------------

        if self.is_open_palm(
            landmark_dict,
            hand_type
        ):

            self.last_action = "PAUSE"
            self.last_action_time = current_time

            stable = self.ai.process(
                gesture=self.last_action,
                dx=dx,
                dy=dy,
                confidence=100
            )

            self.stable_gesture = self.ai.get_gesture()
            self.gesture_confidence = self.ai.get_confidence()

            return stable
        # --------------------------------------------------
        # Adaptive Threshold
        # --------------------------------------------------

        threshold_x = self.ai.get_threshold_x()

        threshold_y = self.ai.get_threshold_y()

        # --------------------------------------------------
        # Ignore Tiny Movement
        # --------------------------------------------------

        if (

            abs(dx) < threshold_x

            and

            abs(dy) < threshold_y

        ):

            return self.ai.get_gesture()

        # --------------------------------------------------
        # Horizontal Movement
        # --------------------------------------------------

        if abs(dx) > abs(dy):

            if dx > threshold_x:

                self.last_action = "RIGHT"

            elif dx < -threshold_x:

                self.last_action = "LEFT"

            else:

                self.last_action = "NONE"

        # --------------------------------------------------
        # Vertical Movement
        # --------------------------------------------------

        else:

            if dy < -threshold_y:

                self.last_action = "JUMP"

            elif dy > threshold_y:

                self.last_action = "SLIDE"

            else:

                self.last_action = "NONE"

            # --------------------------------------------------
            # Execute Cooldown
            # --------------------------------------------------

            if self.last_action != "NONE":

                self.last_action_time = current_time

        # --------------------------------------------------
        # AI Core Processing
        # --------------------------------------------------

        stable = self.ai.process(

        gesture=self.last_action,

        dx=dx,

        dy=dy,

        confidence=100 if self.last_action != "NONE" else 35

        )

        self.stable_gesture = self.ai.get_gesture()

        self.gesture_confidence = self.ai.get_confidence()

        return stable
    # =====================================================
    # Stable Gesture
    # =====================================================

    def get_stable_gesture(self):

        return self.ai.get_gesture()


    # =====================================================
    # Confidence
    # =====================================================

    def get_confidence(self):

        return self.ai.get_confidence()
    # =====================================================
    # AI Statistics
    # =====================================================

    def get_statistics(self):

        return self.ai.get_statistics()
    # =====================================================
    # Adaptive Statistics
    # =====================================================

    def get_adaptive_statistics(

        self

    ):

        return self.ai.get_statistics()

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.previous_center = None

        self.last_action = "NONE"

        self.last_action_time = 0

        self.stable_gesture = "NONE"

        self.gesture_confidence = 0

        self.smoother.reset()

        self.ai.reset()
    # =====================================================
    # Statistics
    # =====================================================

    def get_statistics(self):

        return self.smoother.get_statistics()