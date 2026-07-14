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
    MOVE_THRESHOLD_X,
    MOVE_THRESHOLD_Y,
    MOTION_COOLDOWN
)


class GestureDetector:

    def __init__(self):

        # Previous hand center
        self.previous_center = None

        # Cooldown timer
        self.last_action_time = 0

        # Last detected action (used by UI)
        self.last_action = "NONE"

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

        # No hand

        if hand_center is None:

            self.previous_center = None
            self.last_action = "NONE"

            return self.last_action

        # First frame

        if self.previous_center is None:

            self.previous_center = hand_center

            return self.last_action

        prev_x, prev_y = self.previous_center
        curr_x, curr_y = hand_center

        dx = curr_x - prev_x
        dy = curr_y - prev_y

        # Update previous position every frame
        self.previous_center = hand_center

        current_time = time.time()

        # Cooldown
        if current_time - self.last_action_time < MOTION_COOLDOWN:
            return self.last_action

        # --------------------------------------------------
        # Pause (Open Palm)
        # --------------------------------------------------

        if self.is_open_palm(
            landmark_dict,
            hand_type
        ):

            self.last_action = "PAUSE"
            self.last_action_time = current_time

            print("PAUSE")

            return self.last_action

        # --------------------------------------------------
        # Ignore tiny movement
        # --------------------------------------------------

        if (
            abs(dx) < MOVE_THRESHOLD_X
            and
            abs(dy) < MOVE_THRESHOLD_Y
        ):

            return self.last_action

        # --------------------------------------------------
        # Horizontal movement
        # --------------------------------------------------

        if abs(dx) > abs(dy):

            if dx > MOVE_THRESHOLD_X:

                self.last_action = "RIGHT"

                self.last_action_time = current_time

                print("RIGHT")

                return self.last_action

            elif dx < -MOVE_THRESHOLD_X:

                self.last_action = "LEFT"

                self.last_action_time = current_time

                print("LEFT")

                return self.last_action

        # --------------------------------------------------
        # Vertical movement
        # --------------------------------------------------

        else:

            if dy < -MOVE_THRESHOLD_Y:

                self.last_action = "JUMP"

                self.last_action_time = current_time

                print("JUMP")

                return self.last_action

            elif dy > MOVE_THRESHOLD_Y:

                self.last_action = "SLIDE"

                self.last_action_time = current_time

                print("SLIDE")

                return self.last_action

        return self.last_action

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.previous_center = None
        self.last_action = "NONE"
        self.last_action_time = 0