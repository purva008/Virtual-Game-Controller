import pyautogui
import numpy as np

from config import MOUSE_SMOOTHING


class MouseController:
    """
    Handles mouse movement and scrolling.
    """

    def __init__(self):

        pyautogui.FAILSAFE = False

        self.screen_width, self.screen_height = pyautogui.size()

        self.prev_x = 0
        self.prev_y = 0

        self.smoothing = MOUSE_SMOOTHING

    # --------------------------------------------------
    # Move Mouse
    # --------------------------------------------------

    def move(
        self,
        x,
        y,
        cam_width,
        cam_height
    ):

        screen_x = np.interp(
            x,
            (0, cam_width),
            (0, self.screen_width)
        )

        screen_y = np.interp(
            y,
            (0, cam_height),
            (0, self.screen_height)
        )

        current_x = self.prev_x + (
            screen_x - self.prev_x
        ) / self.smoothing

        current_y = self.prev_y + (
            screen_y - self.prev_y
        ) / self.smoothing

        try:
            pyautogui.moveTo(
                int(current_x),
                int(current_y),
                duration=0
            )
        except Exception:
            pass

        self.prev_x = current_x
        self.prev_y = current_y

    # --------------------------------------------------
    # Drag Mouse
    # --------------------------------------------------

    def drag(
        self,
        x,
        y,
        cam_width,
        cam_height
    ):

        self.move(
            x,
            y,
            cam_width,
            cam_height
        )

    # --------------------------------------------------
    # Scroll
    # --------------------------------------------------

    def scroll(
        self,
        amount
    ):

        try:
            pyautogui.scroll(amount)
        except Exception:
            pass

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.prev_x = 0
        self.prev_y = 0