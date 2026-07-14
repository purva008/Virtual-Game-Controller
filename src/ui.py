"""
=========================================================
UI Module
=========================================================
Draws all information on the OpenCV frame.
=========================================================
"""

import cv2

from config import (
    FONT_SCALE,
    FONT_THICKNESS,
    TEXT_COLOR,
    INFO_COLOR,
    WARNING_COLOR
)


def draw_ui(
    frame,
    gesture,
    hand_type,
    fps,
    bbox=None
):
    """
    Draw UI elements on the video frame.

    Args:
        frame       : OpenCV frame
        gesture     : Detected gesture
        hand_type   : Left / Right / None
        fps         : Frames Per Second
        bbox        : Optional hand bounding box
                      (xmin, ymin, xmax, ymax)
    """

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    cv2.putText(
        frame,
        "AI Virtual Game Controller",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        INFO_COLOR,
        FONT_THICKNESS
    )

    # --------------------------------------------------
    # Gesture
    # --------------------------------------------------

    cv2.putText(
        frame,
        f"Gesture : {gesture}",
        (10, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        TEXT_COLOR,
        FONT_THICKNESS
    )

    # --------------------------------------------------
    # Hand Type
    # --------------------------------------------------

    hand_text = hand_type if hand_type else "Not Detected"

    cv2.putText(
        frame,
        f"Hand : {hand_text}",
        (10, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        TEXT_COLOR,
        FONT_THICKNESS
    )

    # --------------------------------------------------
    # FPS
    # --------------------------------------------------

    cv2.putText(
        frame,
        f"FPS : {fps}",
        (10, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        INFO_COLOR,
        FONT_THICKNESS
    )

    # --------------------------------------------------
    # Detection Status
    # --------------------------------------------------

    if hand_type:

        status = "Hand Detected"
        color = (0, 255, 0)

    else:

        status = "No Hand Detected"
        color = WARNING_COLOR

    cv2.putText(
        frame,
        status,
        (10, 190),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        color,
        FONT_THICKNESS
    )

    # --------------------------------------------------
    # Bounding Box
    # --------------------------------------------------

    if bbox is not None:

        x_min, y_min, x_max, y_max = bbox

        cv2.rectangle(
            frame,
            (x_min, y_min),
            (x_max, y_max),
            (255, 255, 0),
            2
        )

    # --------------------------------------------------
    # Exit Message
    # --------------------------------------------------

    cv2.putText(
        frame,
        "Press 'Q' to Exit",
        (10, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        WARNING_COLOR,
        2
    )

    return frame