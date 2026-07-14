"""
=========================================================
AI Virtual Game Controller
Game Controller
=========================================================
Receives actions from GestureDetector
and executes the corresponding Temple Run controls.
=========================================================
"""

import time

from config import KEY_PRESS_DELAY

from controllers.keyboard_controller import (
    move_left,
    move_right,
    jump,
    slide,
    pause_game
)


class GameController:

    def __init__(self):

        self.previous_action = "NONE"
        self.last_action_time = 0

    # -----------------------------------------------------
    # Execute Action
    # -----------------------------------------------------

    def execute(self, action):

        current_time = time.time()

        # Ignore invalid actions
        if action == "NONE":
            return

        # Prevent duplicate consecutive actions
        if (
            action == self.previous_action and
            current_time - self.last_action_time < KEY_PRESS_DELAY
        ):
            return

        self.previous_action = action
        self.last_action_time = current_time

        # -----------------------------------------
        # LEFT
        # -----------------------------------------

        if action == "LEFT":

            move_left()

            print("⬅ LEFT")

        # -----------------------------------------
        # RIGHT
        # -----------------------------------------

        elif action == "RIGHT":

            move_right()

            print("➡ RIGHT")

        # -----------------------------------------
        # JUMP
        # -----------------------------------------

        elif action == "JUMP":

            jump()

            print("⬆ JUMP")

        # -----------------------------------------
        # SLIDE
        # -----------------------------------------

        elif action == "SLIDE":

            slide()

            print("⬇ SLIDE")

        # -----------------------------------------
        # PAUSE
        # -----------------------------------------

        elif action == "PAUSE":

            pause_game()

            print("⏸ PAUSE")

    # -----------------------------------------------------
    # Reset
    # -----------------------------------------------------

    def reset(self):

        self.previous_action = "NONE"
        self.last_action_time = 0