import pyautogui

pyautogui.FAILSAFE = False


def scroll_up():
    pyautogui.scroll(300)


def scroll_down():
    pyautogui.scroll(-300)