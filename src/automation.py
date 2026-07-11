import pyautogui

pyautogui.FAILSAFE = False


def move_left():
    pyautogui.press("a")


def move_right():
    pyautogui.press("d")


def jump():
    pyautogui.press("space")


def attack():
    pyautogui.click()


def pause_game():
    pyautogui.press("esc")