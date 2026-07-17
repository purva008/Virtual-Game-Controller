"""
=========================================================
AI Virtual Game Controller
Professional Splash Screen
Version 2.0
=========================================================

Professional splash screen with real-time loading updates.

Author : Uttam Ahire
=========================================================
"""

import tkinter as tk
from tkinter import ttk

from config import (
    APP_NAME,
    APP_VERSION,
    APP_SUBTITLE,
    DEVELOPER_NAME
)


class SplashScreen:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(APP_NAME)

        self.root.geometry("700x420")

        self.root.configure(bg="#1E1E1E")

        self.root.resizable(False, False)

        self.root.overrideredirect(True)

        self.center_window()

        self.build_ui()

    # =====================================================
    # Center Window
    # =====================================================

    def center_window(self):

        self.root.update_idletasks()

        width = 700
        height = 420

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.root.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # =====================================================
    # Build UI
    # =====================================================

    def build_ui(self):

        tk.Label(

            self.root,

            text="🎮",

            font=("Segoe UI Emoji", 44),

            fg="#00D8FF",

            bg="#1E1E1E"

        ).pack(pady=(20, 5))

        tk.Label(

            self.root,

            text=APP_NAME,

            font=("Segoe UI", 24, "bold"),

            fg="#00D8FF",

            bg="#1E1E1E"

        ).pack()

        tk.Label(

            self.root,

            text=f"Version {APP_VERSION}",

            font=("Segoe UI", 11),

            fg="white",

            bg="#1E1E1E"

        ).pack()

        tk.Label(

            self.root,

            text=APP_SUBTITLE,

            font=("Segoe UI", 12),

            fg="#D0D0D0",

            bg="#1E1E1E"

        ).pack(pady=10)

        ttk.Separator(

            self.root,

            orient="horizontal"

        ).pack(

            fill="x",

            padx=40,

            pady=15

        )

        # -------------------------
        # Status Label
        # -------------------------

        self.status_label = tk.Label(

            self.root,

            text="Starting...",

            font=("Segoe UI", 11),

            fg="#90EE90",

            bg="#1E1E1E"

        )

        self.status_label.pack(pady=10)

        # -------------------------
        # Progress Bar
        # -------------------------

        style = ttk.Style()

        style.theme_use("default")

        style.configure(

            "green.Horizontal.TProgressbar",

            troughcolor="#2E2E2E",

            background="#00C853",

            thickness=18

        )

        self.progress = ttk.Progressbar(

            self.root,

            orient="horizontal",

            mode="determinate",

            maximum=100,

            length=520,

            style="green.Horizontal.TProgressbar"

        )

        self.progress.pack(pady=10)

        # -------------------------
        # Percentage
        # -------------------------

        self.percent_label = tk.Label(

            self.root,

            text="0%",

            font=("Segoe UI", 10, "bold"),

            fg="white",

            bg="#1E1E1E"

        )

        self.percent_label.pack()

        # -------------------------
        # Footer
        # -------------------------

        tk.Label(

            self.root,

            text=f"Developed by {DEVELOPER_NAME}",

            font=("Segoe UI", 10),

            fg="#888888",

            bg="#1E1E1E"

        ).pack(side="bottom", pady=15)

    # =====================================================
    # Update Progress
    # =====================================================

    def update_progress(

        self,

        value,

        message

    ):

        self.progress["value"] = value

        self.status_label.config(

            text=message

        )

        self.percent_label.config(

            text=f"{value}%"

        )

        self.root.update()

    # =====================================================
    # Show
    # =====================================================

    def show(self):

        self.root.update()

    # =====================================================
    # Close
    # =====================================================

    def close(self):

        self.root.destroy()


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    import time

    splash = SplashScreen()

    splash.show()

    steps = [

        "Initializing Camera...",

        "Loading MediaPipe...",

        "Loading Gesture Engine...",

        "Loading Controller...",

        "Preparing Dashboard...",

        "Ready!"

    ]

    progress = 0

    for step in steps:

        progress += 20

        splash.update_progress(

            progress,

            step

        )

        time.sleep(0.7)

    splash.close()