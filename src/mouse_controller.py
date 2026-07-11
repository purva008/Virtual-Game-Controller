import pyautogui

pyautogui.FAILSAFE = False

screen_width, screen_height = pyautogui.size()

prev_x = 0
prev_y = 0

smoothening = 7

clicked = False
right_clicked = False
dragging = False


def move_mouse(x, y, cam_width, cam_height):
    global prev_x, prev_y

    screen_x = int((x / cam_width) * screen_width)
    screen_y = int((y / cam_height) * screen_height)

    current_x = prev_x + (screen_x - prev_x) / smoothening
    current_y = prev_y + (screen_y - prev_y) / smoothening

    pyautogui.moveTo(current_x, current_y)

    prev_x = current_x
    prev_y = current_y


def left_click():
    global clicked

    if not clicked:
        pyautogui.click()
        clicked = True


def right_click():
    global right_clicked

    if not right_clicked:
        pyautogui.click(button="right")
        right_clicked = True


def start_drag():
    global dragging

    if not dragging:
        pyautogui.mouseDown()
        dragging = True


def stop_drag():
    global dragging

    if dragging:
        pyautogui.mouseUp()
        dragging = False


def reset_click():
    global clicked, right_clicked

    clicked = False
    right_clicked = False