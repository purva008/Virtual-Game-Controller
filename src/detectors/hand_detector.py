"""
=========================================================
AI Virtual Game Controller
Hand Detector
=========================================================
Uses MediaPipe Hands to:
1. Detect hand
2. Extract landmarks
3. Calculate hand center
4. Calculate bounding box
=========================================================
"""

import cv2
import mediapipe as mp
import math

from config import (
    MAX_HANDS,
    DETECTION_CONFIDENCE,
    TRACKING_CONFIDENCE
)


class HandDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            model_complexity=1,
            min_detection_confidence=DETECTION_CONFIDENCE,
            min_tracking_confidence=TRACKING_CONFIDENCE
        )

        self.mp_draw = mp.solutions.drawing_utils

        self.landmark_style = self.mp_draw.DrawingSpec(
            color=(0, 255, 0),
            thickness=2,
            circle_radius=3
        )

        self.connection_style = self.mp_draw.DrawingSpec(
            color=(255, 0, 0),
            thickness=2
        )

        self.results = None

    # ---------------------------------------------------
    # Detect Hand
    # ---------------------------------------------------

    def find_hands(self, frame, draw=True):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        rgb.flags.writeable = False
        self.results = self.hands.process(rgb)
        rgb.flags.writeable = True

        if draw and self.results.multi_hand_landmarks:

            for hand_landmarks in self.results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.landmark_style,
                    self.connection_style
                )

        return frame

    # ---------------------------------------------------
    # Get Hand Information
    # ---------------------------------------------------

    def get_landmarks(self, frame):

        landmarks = []
        landmark_dict = {}
        hand_type = None
        bbox = None
        hand_center = None

        if not self.results or not self.results.multi_hand_landmarks:
            return (
                landmarks,
                landmark_dict,
                hand_type,
                bbox,
                hand_center
            )

        h, w, _ = frame.shape

        hand = self.results.multi_hand_landmarks[0]

        x_list = []
        y_list = []

        for idx, lm in enumerate(hand.landmark):

            x = int(lm.x * w)
            y = int(lm.y * h)

            landmarks.append((idx, x, y))
            landmark_dict[idx] = (x, y)

            x_list.append(x)
            y_list.append(y)

        # -----------------------------
        # Bounding Box
        # -----------------------------

        x_min = min(x_list)
        y_min = min(y_list)
        x_max = max(x_list)
        y_max = max(y_list)

        bbox = (
            x_min,
            y_min,
            x_max - x_min,
            y_max - y_min
        )

        # -----------------------------
        # Hand Center
        # -----------------------------

        center_x = int(sum(x_list) / len(x_list))
        center_y = int(sum(y_list) / len(y_list))

        hand_center = (
            center_x,
            center_y
        )

        # Draw center point

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
            (center_x + 10, center_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2
        )

        # -----------------------------
        # Hand Type
        # -----------------------------

        if self.results.multi_handedness:

            hand_type = (
                self.results
                .multi_handedness[0]
                .classification[0]
                .label
            )

        return (
            landmarks,
            landmark_dict,
            hand_type,
            bbox,
            hand_center
        )

    # ---------------------------------------------------
    # Finger State
    # ---------------------------------------------------

    def get_finger_state(
        self,
        landmark_dict,
        hand_type="Right"
    ):

        if len(landmark_dict) != 21:
            return [0, 0, 0, 0, 0]

        fingers = []

        # Thumb

        if hand_type == "Right":

            fingers.append(
                int(
                    landmark_dict[4][0] >
                    landmark_dict[3][0]
                )
            )

        else:

            fingers.append(
                int(
                    landmark_dict[4][0] <
                    landmark_dict[3][0]
                )
            )

        tip_ids = [8, 12, 16, 20]
        pip_ids = [6, 10, 14, 18]

        for tip, pip in zip(
            tip_ids,
            pip_ids
        ):

            fingers.append(
                int(
                    landmark_dict[tip][1] <
                    landmark_dict[pip][1]
                )
            )

        return fingers

    # ---------------------------------------------------
    # Distance
    # ---------------------------------------------------

    def calculate_distance(
        self,
        point1,
        point2
    ):

        x1, y1 = point1
        x2, y2 = point2

        return math.hypot(
            x2 - x1,
            y2 - y1
        )

    # ---------------------------------------------------
    # Release
    # ---------------------------------------------------

    def close(self):

        self.hands.close()