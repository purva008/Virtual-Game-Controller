"""
=========================================================
AI Virtual Game Controller
Professional Dashboard Engine
=========================================================

Main dashboard coordinator.

Responsible for

✓ Left Dashboard
✓ Camera Feed Overlay
✓ Motion Trail
✓ Bounding Boxes
✓ Gesture Display
✓ Runtime
✓ FPS
✓ Action History

Author : Uttam Ahire
Version : 3.0
=========================================================
"""
import cv2

from ui.panels import DashboardPanel

from ui.theme import *

from config import APP_VERSION
class Dashboard:
    """
    Professional Dashboard Engine.
    """

    def __init__(self):

        self.panel = DashboardPanel()
    # =====================================================
    # Motion Trail
    # =====================================================

    def draw_motion_trail(

        self,

        frame,

        trail

    ):

        if trail is None:

            return

        if len(trail) < 2:

            return

        for i in range(1, len(trail)):

            cv2.line(

                frame,

                trail[i - 1],

                trail[i],

                TRAIL,

                2

            )
    # =====================================================
    # Bounding Box
    # =====================================================

    def draw_bounding_box(

        self,

        frame,

        bbox

    ):

        if bbox is None:

            return

        x, y, w, h = bbox

        cv2.rectangle(

            frame,

            (x, y),

            (x + w, y + h),

            BOUNDING_BOX,

            2

        )
    # =====================================================
    # Hand Center
    # =====================================================

    def draw_hand_center(

        self,

        frame,

        center

    ):

        if center is None:

            return

        cv2.circle(

            frame,

            center,

            6,

            HAND_CENTER,

            -1

        )
    # =====================================================
    # Gesture
    # =====================================================

    def draw_gesture(

        self,

        frame,

        gesture

    ):

        color = GESTURE_ACTIVE

        if gesture in (None, "NONE"):

            color = SUBTEXT

            gesture = "Waiting..."

        cv2.putText(

            frame,

            f"Gesture : {gesture}",

            (365, 40),

            HEADER_FONT,

            HEADER_SCALE,

            color,

            HEADER_THICKNESS

        )
    # =====================================================
    # FPS
    # =====================================================

    def draw_fps(

        self,

        frame,

        fps

    ):

        cv2.putText(

            frame,

            f"FPS : {fps}",

            (365, 72),

            TEXT_FONT,

            TEXT_SCALE,

            FPS,

            TEXT_THICKNESS

        )
    # =====================================================
    # Runtime
    # =====================================================

    def draw_runtime(

        self,

        frame,

        runtime

    ):

        cv2.putText(

            frame,

            f"Runtime : {int(runtime)} sec",

            (365, 98),

            SMALL_FONT,

            SMALL_SCALE,

            TEXT,

            SMALL_THICKNESS

        )
    # =====================================================
    # Draw Dashboard
    # =====================================================

    def draw(

        self,

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

        self.panel.draw(

            frame,

            APP_VERSION,

            system_info,

            average_fps,

            camera_stats,

            confidence,

            history

        )

        self.draw_motion_trail(

            frame,

            motion_trail

        )

        self.draw_bounding_box(

            frame,

            bbox

        )

        self.draw_hand_center(

            frame,

            hand_center

        )

        self.draw_gesture(

            frame,

            gesture

        )

        self.draw_fps(

            frame,

            fps

        )

        self.draw_runtime(

            frame,

            runtime

        )

        return frame