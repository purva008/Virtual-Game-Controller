"""
=========================================================
AI Virtual Game Controller
Keyboard Controller
=========================================================
Handles keyboard automation for Temple Run.
=========================================================
"""

import time
import pyautogui

from config import KEY_PRESS_DELAY

pyautogui.FAILSAFE = False

last_action_time = 0


def press_key(key):
    """
    Press a keyboard key with cooldown.
    """

    global last_action_time

    current_time = time.time()

    if current_time - last_action_time >= KEY_PRESS_DELAY:

        pyautogui.press(key)

        last_action_time = current_time


# =========================================================
# Temple Run Controls
# =========================================================

def move_left():
    press_key("left")


def move_right():
    press_key("right")


def jump():
    press_key("up")


def slide():
    press_key("down")


def pause_game():
    press_key("esc")