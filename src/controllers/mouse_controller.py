import pyautogui

pyautogui.FAILSAFE = False

screen_width, screen_height = pyautogui.size()

# Previous cursor position
prev_x = 0
prev_y = 0

# Smoothing factor (higher = smoother)
from config import MOUSE_SMOOTHING
SMOOTHING = MOUSE_SMOOTHING

def move_mouse(x, y, cam_width, cam_height):
    global prev_x, prev_y

    # Convert camera coordinates to screen coordinates
    screen_x = int((x / cam_width) * screen_width)
    screen_y = int((y / cam_height) * screen_height)

    # Apply smoothing
    smooth_x = prev_x + (screen_x - prev_x) / SMOOTHING
    smooth_y = prev_y + (screen_y - prev_y) / SMOOTHING

    pyautogui.moveTo(int(smooth_x), int(smooth_y), duration=0)

    prev_x = smooth_x
    prev_y = smooth_y