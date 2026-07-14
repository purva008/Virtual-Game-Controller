import time

import pyautogui

from config import CLICK_DELAY


class ClickController:
    """
    Handles all mouse click actions.
    """

    def __init__(self):

        pyautogui.FAILSAFE = False

        self.last_click = 0

        self.dragging = False

    # --------------------------------------------------
    # Cooldown Check
    # --------------------------------------------------

    def _can_click(self):

        current_time = time.time()

        if current_time - self.last_click >= CLICK_DELAY:

            self.last_click = current_time
            return True

        return False

    # --------------------------------------------------
    # Left Click
    # --------------------------------------------------

    def left_click(self):

        if not self._can_click():
            return

        try:
            pyautogui.click(button="left")
        except Exception:
            pass

    # --------------------------------------------------
    # Right Click
    # --------------------------------------------------

    def right_click(self):

        if not self._can_click():
            return

        try:
            pyautogui.click(button="right")
        except Exception:
            pass

    # --------------------------------------------------
    # Double Click
    # --------------------------------------------------

    def double_click(self):

        if not self._can_click():
            return

        try:
            pyautogui.doubleClick()
        except Exception:
            pass

    # --------------------------------------------------
    # Start Drag
    # --------------------------------------------------

    def start_drag(self):

        if self.dragging:
            return

        try:
            pyautogui.mouseDown()
            self.dragging = True
        except Exception:
            pass

    # --------------------------------------------------
    # Stop Drag
    # --------------------------------------------------

    def stop_drag(self):

        if not self.dragging:
            return

        try:
            pyautogui.mouseUp()
            self.dragging = False
        except Exception:
            pass

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.stop_drag()

        self.last_click = 0