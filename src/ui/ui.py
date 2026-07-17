"""
=========================================================
AI Virtual Game Controller
Professional UI Engine
Version 4.0
=========================================================

This module serves as the main UI entry point.

Responsibilities
----------------
✓ Initialize Dashboard Engine
✓ Forward drawing requests
✓ Manage UI helper utilities
✓ Keep compatibility with main.py

Architecture
------------
main.py
    ↓
draw_ui()
    ↓
Dashboard.draw()
    ↓
Panels
    ↓
Cards
    ↓
Theme

Author : Uttam Ahire
Version : 4.0
=========================================================
"""

import cv2

from ui.dashboard import Dashboard

from ui.theme import *

# =========================================================
# Dashboard Engine
# =========================================================

dashboard = Dashboard()

# =========================================================
# UI Version
# =========================================================

UI_VERSION = "4.0"

# =========================================================
# Helper Functions
# =========================================================

def format_runtime(runtime):
    """
    Convert runtime (seconds)
    into HH:MM:SS format.
    """

    runtime = int(runtime)

    hours = runtime // 3600

    minutes = (runtime % 3600) // 60

    seconds = runtime % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def safe_text(value):
    """
    Prevent None values from appearing
    on the dashboard.
    """

    if value is None:

        return "--"

    return str(value)


def safe_percentage(value):
    """
    Clamp percentage values
    between 0 and 100.
    """

    if value is None:

        return 0

    return max(0, min(100, float(value)))


# =========================================================
# Default Camera Statistics
# =========================================================

DEFAULT_CAMERA_STATS = {

    "state": "UNKNOWN",

    "status": "Unavailable",

    "retry_count": 0,

    "total_failures": 0,

    "total_recoveries": 0,

    "success_rate": 100.0,

    "frame_timeout": 0,

    "max_retries": 0

}

# =========================================================
# Default System Information
# =========================================================

DEFAULT_SYSTEM_INFO = {

    "cpu": 0,

    "ram": 0,

    "temperature": 0,

    "os": "--",

    "python": "--",

    "opencv": "--",

    "mediapipe": "--"

}

# =========================================================
# UI Ready
# =========================================================

print(f"[UI] Professional UI Engine v{UI_VERSION} Loaded")
# =========================================================
# Motion Trail
# =========================================================

def draw_motion_trail(frame, motion_trail):
    """
    Draw hand motion trail.
    """

    dashboard.draw_motion_trail(

        frame,

        motion_trail

    )


# =========================================================
# Bounding Box
# =========================================================

def draw_bounding_box(frame, bbox):
    """
    Draw hand bounding box.
    """

    dashboard.draw_bounding_box(

        frame,

        bbox

    )


# =========================================================
# Hand Center
# =========================================================

def draw_hand_center(frame, center):
    """
    Draw hand center point.
    """

    dashboard.draw_hand_center(

        frame,

        center

    )


# =========================================================
# Gesture Overlay
# =========================================================

def draw_gesture(frame, gesture):
    """
    Draw current gesture.
    """

    dashboard.draw_gesture(

        frame,

        safe_text(gesture)

    )


# =========================================================
# FPS Overlay
# =========================================================

def draw_fps(frame, fps):
    """
    Draw current FPS.
    """

    dashboard.draw_fps(

        frame,

        fps

    )


# =========================================================
# Runtime Overlay
# =========================================================

def draw_runtime(frame, runtime):
    """
    Draw application runtime.
    """

    dashboard.draw_runtime(

        frame,

        format_runtime(runtime)

    )


# =========================================================
# System Information
# =========================================================

def normalize_system_info(system_info):
    """
    Ensure every required key exists.
    """

    if system_info is None:

        return DEFAULT_SYSTEM_INFO.copy()

    info = DEFAULT_SYSTEM_INFO.copy()

    info.update(system_info)

    return info


# =========================================================
# Camera Statistics
# =========================================================

def normalize_camera_stats(camera_stats):
    """
    Ensure every required key exists.
    """

    if camera_stats is None:

        return DEFAULT_CAMERA_STATS.copy()

    stats = DEFAULT_CAMERA_STATS.copy()

    stats.update(camera_stats)

    return stats


# =========================================================
# Average FPS
# =========================================================

def normalize_average_fps(value):
    """
    Prevent None values.
    """

    if value is None:

        return 0

    return float(value)
# =========================================================
# Dashboard Integration
# =========================================================

def prepare_dashboard_data(

    gesture,

    confidence,

    history,

    fps,

    runtime,

    average_fps,

    system_info,

    camera_stats

):
    """
    Prepare all dashboard data.
    """

    data = {}

    # --------------------------------------------
    # Gesture
    # --------------------------------------------

    data["gesture"] = safe_text(

        gesture

    )
    # --------------------------------------------
    # Confidence
    # --------------------------------------------

    data["confidence"] = safe_percentage(

        confidence

    )

    # --------------------------------------------
    # History
    # --------------------------------------------

    data["history"] = history if history is not None else []

    # --------------------------------------------
    # FPS
    # --------------------------------------------

    data["fps"] = float(

        fps if fps is not None else 0

    )

    # --------------------------------------------
    # Runtime
    # --------------------------------------------

    data["runtime"] = runtime

    # --------------------------------------------
    # Average FPS
    # --------------------------------------------

    data["average_fps"] = normalize_average_fps(

        average_fps

    )

    # --------------------------------------------
    # System Information
    # --------------------------------------------

    data["system_info"] = normalize_system_info(

        system_info

    )

    # --------------------------------------------
    # Camera Statistics
    # --------------------------------------------

    data["camera_stats"] = normalize_camera_stats(

        camera_stats

    )

    return data


# =========================================================
# Dashboard Renderer
# =========================================================

def render_dashboard(

    frame,

    bbox,

    hand_center,

    motion_trail,

    dashboard_data

):
    """
    Render complete dashboard.
    """

    return dashboard.draw(

        frame=frame,

        bbox=bbox,

        hand_center=hand_center,

        motion_trail=motion_trail,

        gesture=dashboard_data["gesture"],

        confidence=dashboard_data["confidence"],

        history=dashboard_data["history"],


        fps=dashboard_data["fps"],

        runtime=dashboard_data["runtime"],

        average_fps=dashboard_data["average_fps"],

        system_info=dashboard_data["system_info"],

        camera_stats=dashboard_data["camera_stats"]

    )


# =========================================================
# Future Extensions
# =========================================================

def update_action_history(history):
    """
    Placeholder for future
    action history panel.
    """

    return history


def update_notification_queue(message):
    """
    Placeholder for future
    notification system.
    """

    return message


def update_debug_information(debug_data):
    """
    Placeholder for future
    developer mode.
    """

    return debug_data


# =========================================================
# UI Compatibility Layer
# =========================================================

def process_ui(

    frame,

    bbox,

    hand_center,

    motion_trail,

    gesture,

    confidence,

    history,

    fps,

    runtime,

    average_fps,

    system_info,

    camera_stats

):
    """
    Main processing layer before drawing.
    """

    dashboard_data = prepare_dashboard_data(

        gesture,

        confidence,

        history,

        fps,

        runtime,

        average_fps,

        system_info,

        camera_stats

    )

    frame = render_dashboard(

        frame,

        bbox,

        hand_center,

        motion_trail,

        dashboard_data

    )

    return frame
# =========================================================
# Main UI Function
# =========================================================

def draw_ui(

    frame,

    gesture=None,

    hand_type=None,

    fps=0,

    runtime=0,

    bbox=None,

    hand_center=None,

    history=None,

    game_connected=False,

    confidence=0,

    motion_trail=None,

    frame_count=0,

    action_count=0,

    average_fps=0,

    system_info=None,

    camera_stats=None

):
    """
    Professional UI Entry Point

    Parameters
    ----------
    frame : OpenCV Frame

    gesture : Current Gesture

    fps : Current FPS

    runtime : Runtime

    bbox : Hand Bounding Box

    hand_center : Hand Center

    motion_trail : Motion Trail

    average_fps : Average FPS

    system_info : System Information

    camera_stats : Camera Recovery Statistics
    """

    # -----------------------------------------
    # Normalize Incoming Data
    # -----------------------------------------

    if frame is None:

        return None

    if system_info is None:

        system_info = DEFAULT_SYSTEM_INFO.copy()

    if camera_stats is None:

        camera_stats = DEFAULT_CAMERA_STATS.copy()

    if motion_trail is None:

        motion_trail = []

    # -----------------------------------------
    # Render Dashboard
    # -----------------------------------------

    frame = process_ui(

        frame=frame,

        bbox=bbox,

        hand_center=hand_center,

        motion_trail=motion_trail,

        gesture=gesture,

        confidence=confidence,

        history=history,


        fps=fps,

        runtime=runtime,

        average_fps=average_fps,

        system_info=system_info,

        camera_stats=camera_stats

    )

    return frame


# =========================================================
# Module Information
# =========================================================

def get_ui_version():
    """
    Return current UI version.
    """

    return UI_VERSION


def get_dashboard():
    """
    Return dashboard instance.
    """

    return dashboard


# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    print("=" * 55)

    print(" AI Virtual Game Controller")

    print(" Professional UI Engine")

    print(f" Version : {UI_VERSION}")

    print("=" * 55)

    print("Dashboard Initialized Successfully")

    print("UI Module Ready")