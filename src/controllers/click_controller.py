from pynput.mouse import Button, Controller

mouse = Controller()

dragging = False

def left_click():
    mouse.click(Button.left, 1)

def right_click():
    mouse.click(Button.right, 1)

def start_drag():
    global dragging
    if not dragging:
        mouse.press(Button.left)
        dragging = True

def stop_drag():
    global dragging
    if dragging:
        mouse.release(Button.left)
        dragging = False