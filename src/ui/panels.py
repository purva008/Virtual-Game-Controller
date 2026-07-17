"""
=========================================================
AI Virtual Game Controller
Professional Dashboard Panels
=========================================================

Responsible for drawing the left dashboard.

Uses reusable cards.

Author : Uttam Ahire
Version : 3.0
=========================================================
"""
import cv2

from ui.cards import DashboardCard

from ui.theme import *
class DashboardPanel:
    """
    Professional Dashboard Panel.
    """

    def __init__(self):

        self.card = DashboardCard()
    # =====================================================
    # Background
    # =====================================================

    def draw_background(

        self,

        frame

    ):

        cv2.rectangle(

            frame,

            (0, 0),

            (PANEL_WIDTH, frame.shape[0]),

            PANEL_BACKGROUND,

            -1

        )

        cv2.line(

            frame,

            (PANEL_WIDTH, 0),

            (PANEL_WIDTH, frame.shape[0]),

            BORDER,

            2

        )
    # =====================================================
    # Title
    # =====================================================

    def draw_title(

        self,

        frame

    ):

        cv2.putText(

            frame,

            "AI Virtual Game Controller",

            (18, 40),

            TITLE_FONT,

            0.72,

            TITLE,

            TITLE_THICKNESS

        )
    # =====================================================
    # Version
    # =====================================================

    def draw_version(

        self,

        frame,

        version

    ):

        cv2.putText(

            frame,

            f"Version {version}",

            (20, 65),

            SMALL_FONT,

            SMALL_SCALE,

            SUBTEXT,

            SMALL_THICKNESS

        )
    # =====================================================
    # System Section
    # =====================================================

    def draw_system_section(

        self,

        frame,

        system_info

    ):

        x = 15

        y = 90

        w = PANEL_WIDTH - 30

        h = 78

        self.card.draw_info_card(

            frame,

            "CPU",

            f"{system_info['cpu']}%",

            x,

            y,

            w,

            h

        )

        self.card.draw_info_card(

            frame,

            "RAM",

            f"{system_info['ram']}%",

            x,

            y + 90,

            w,

            h

        )
    # =====================================================
    # Performance
    # =====================================================

    def draw_performance_section(

        self,

        frame,

        average_fps

    ):

        x = 15

        y = 275

        w = PANEL_WIDTH - 30

        h = 78

        self.card.draw_info_card(

            frame,

            "Average FPS",

            f"{average_fps:.1f}",

            x,

            y,

            w,

            h

        )
    # =====================================================
    # Camera
    # =====================================================

    def draw_camera_section(

        self,

        frame,

        camera_stats

    ):

        self.card.draw_camera_card(

            frame,

            camera_stats,

            15,

            365,

            PANEL_WIDTH - 30,

            78

        )
    # =====================================================
    # AI Confidence
    # =====================================================

    def draw_confidence_section(

        self,

        frame,

        confidence

    ):

        self.card.draw_confidence_card(

            frame,

            confidence,

            15,

            455,

            PANEL_WIDTH - 30,

            90

        )
    # =====================================================
    # Recent Actions
    # =====================================================

    def draw_action_history_section(

        self,

        frame,

        history

    ):

        x = 15

        y = 560

        width = PANEL_WIDTH - 30

        height = 170

        self.card.draw_background(

            frame,

            x,

            y,

            width,

            height

        )

        self.card.draw_title(

            frame,

            "Recent Actions",

            x + 12,

            y + 24

        )

        self.card.draw_separator(

            frame,

            x + 10,

            y + 34,

            width - 20

        )

        row_y = y + 58

        max_items = 6

        recent = list(history)[-max_items:]

        if len(recent) == 0:

            self.card.draw_label(

                frame,

                "No actions yet",

                x + 14,

                row_y

            )

            return

        for action in reversed(recent):

            self.card.draw_label(

                frame,

                f"• {action}",

                x + 14,

                row_y

            )

            row_y += 22
    # =====================================================
    # Draw Dashboard
    # =====================================================

    def draw(

        self,

        frame,

        version,

        system_info,

        average_fps,

        camera_stats,
        
        confidence,

        history

    ):

        self.draw_background(

            frame

        )

        self.draw_title(

            frame

        )

        self.draw_version(

            frame,

            version

        )

        self.draw_system_section(

            frame,

            system_info

        )

        self.draw_performance_section(

            frame,

            average_fps

        )

        self.draw_camera_section(

            frame,

            camera_stats

        )

        self.draw_confidence_section(

            frame,

            confidence

        )
        self.draw_action_history_section(

            frame,

            history

        )

        return frame