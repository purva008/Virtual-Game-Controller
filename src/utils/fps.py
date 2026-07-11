import time

class FPSCounter:

    def __init__(self):
        self.previous_time = time.time()
        self.start_time = time.time()

    def get_fps(self):
        current_time = time.time()
        fps = 1 / (current_time - self.previous_time)
        self.previous_time = current_time
        return int(fps)

    def get_session_time(self):
        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        return f"{minutes:02}:{seconds:02}"