import time

from config import GESTURE_STABILITY


class GestureStabilizer:
    """
    Ensures that a gesture remains unchanged for a
    minimum amount of time before it is considered valid.
    """

    def __init__(self, delay=GESTURE_STABILITY):

        self.delay = delay

        self.previous_gesture = None

        self.start_time = time.time()

    def is_stable(self, current_gesture):

        if current_gesture != self.previous_gesture:

            self.previous_gesture = current_gesture
            self.start_time = time.time()

            return False

        return (time.time() - self.start_time) >= self.delay

    def reset(self):

        self.previous_gesture = None
        self.start_time = time.time()