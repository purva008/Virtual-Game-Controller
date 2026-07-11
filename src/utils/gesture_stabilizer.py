import time

class GestureStabilizer:

    def __init__(self, delay=0.5):
        self.delay = delay
        self.previous_gesture = None
        self.start_time = time.time()

    def is_stable(self, current_gesture):

        if current_gesture != self.previous_gesture:
            self.previous_gesture = current_gesture
            self.start_time = time.time()
            return False

        if time.time() - self.start_time >= self.delay:
            return True

        return False