import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mpDraw = mp.solutions.drawing_utils

    def detectHands(self, frame, draw=True):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb)
        print(self.results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:

            for hand in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(
                        frame,
                        hand,
                        self.mpHands.HAND_CONNECTIONS
                    )

        return frame

    def findPosition(self, frame):

        landmarkList = []

        if self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            h, w, c = frame.shape

            for id, lm in enumerate(hand.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                landmarkList.append([id, cx, cy])

        return landmarkList

    def fingersUp(self, landmarkList):

        fingers = []

        # Thumb
        if landmarkList[4][1] > landmarkList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other four fingers
        tips = [8, 12, 16, 20]

        for tip in tips:
            if landmarkList[tip][2] < landmarkList[tip - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers