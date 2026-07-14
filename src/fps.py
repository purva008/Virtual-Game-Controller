import time


class FPSCounter:
    """
    Calculates Frames Per Second (FPS).
    """

    def __init__(self):
        self.previous_time = 0

    def update(self):
        """
        Returns the current FPS.
        """

        current_time = time.time()

        fps = 0

        if self.previous_time != 0:
            fps = 1 / (current_time - self.previous_time)

        self.previous_time = current_time

        return int(fps)