"""
=========================================================
AI Virtual Game Controller
Professional Card Engine
=========================================================

Reusable Dashboard Cards

✓ Information Card

✓ Status Card

✓ Progress Card

✓ Value Card

Author : Uttam Ahire

Version : 3.0
=========================================================
"""
import cv2

from ui.theme import *
class DashboardCard:
    """
    Reusable Dashboard Card.
    """

    def __init__(self):

        self.radius = 8
    # =====================================================
    # Card Background
    # =====================================================

    def draw_background(

        self,

        frame,

        x,

        y,

        width,

        height

    ):

        cv2.rectangle(

            frame,

            (x, y),

            (x + width, y + height),

            CARD_BACKGROUND,

            -1

        )

        cv2.rectangle(

            frame,

            (x, y),

            (x + width, y + height),

            CARD_BORDER,

            1

        )
    # =====================================================
    # Title
    # =====================================================

    def draw_title(

        self,

        frame,

        title,

        x,

        y

    ):

        cv2.putText(

            frame,

            title,

            (x, y),

            HEADER_FONT,

            HEADER_SCALE,

            HEADER,

            HEADER_THICKNESS

        )
    # =====================================================
    # Value
    # =====================================================

    def draw_value(

        self,

        frame,

        value,

        x,

        y

    ):

        cv2.putText(

            frame,

            str(value),

            (x, y),

            TITLE_FONT,

            TITLE_SCALE,

            VALUE,

            TITLE_THICKNESS

        )
    # =====================================================
    # Label
    # =====================================================

    def draw_label(

        self,

        frame,

        label,

        x,

        y

    ):

        cv2.putText(

            frame,

            label,

            (x, y),

            TEXT_FONT,

            TEXT_SCALE,

            TEXT,

            TEXT_THICKNESS

        )
    # =====================================================
    # Separator
    # =====================================================

    def draw_separator(

        self,

        frame,

        x,

        y,

        width

    ):

        cv2.line(

            frame,

            (x, y),

            (x + width, y),

            SEPARATOR,

            1

        )
    # =====================================================
    # Information Card
    # =====================================================

    def draw_info_card(

        self,

        frame,

        title,

        value,

        x,

        y,

        width,

        height

    ):

        self.draw_background(

            frame,

            x,

            y,

            width,

            height

        )

        self.draw_title(

            frame,

            title,

            x + 12,

            y + 24

        )

        self.draw_separator(

            frame,

            x + 10,

            y + 34,

            width - 20

        )

        self.draw_value(

            frame,

            value,

            x + 18,

            y + 62

        )
    # =====================================================
    # Status Card
    # =====================================================

    def draw_status_card(

        self,

        frame,

        title,

        status,

        color,

        x,

        y,

        width,

        height

    ):

        self.draw_background(

            frame,

            x,

            y,

            width,

            height

        )

        self.draw_title(

            frame,

            title,

            x + 12,

            y + 24

        )

        cv2.circle(

            frame,

            (x + 22, y + 58),

            7,

            color,

            -1

        )

        cv2.putText(

            frame,

            status,

            (x + 38, y + 64),

            TEXT_FONT,

            TEXT_SCALE,

            TEXT,

            TEXT_THICKNESS

        )
    # =====================================================
    # Progress Bar
    # =====================================================

    def draw_progress_bar(

        self,

        frame,

        percentage,

        x,

        y,

        width,

        height

    ):

        cv2.rectangle(

            frame,

            (x, y),

            (x + width, y + height),

            PROGRESS_BACKGROUND,

            -1

        )

        fill = int(

            width *

            max(

                0,

                min(

                    percentage,

                    100

                )

            ) / 100

        )

        cv2.rectangle(

            frame,

            (x, y),

            (x + fill, y + height),

            PROGRESS_FILL,

            -1

        )
    # =====================================================
    # Progress Card
    # =====================================================

    def draw_progress_card(

        self,

        frame,

        title,

        percentage,

        x,

        y,

        width,

        height

    ):

        self.draw_background(

            frame,

            x,

            y,

            width,

            height

        )

        self.draw_title(

            frame,

            title,

            x + 12,

            y + 24

        )

        self.draw_progress_bar(

            frame,

            percentage,

            x + 12,

            y + 42,

            width - 24,

            18

        )

        self.draw_label(

            frame,

            f"{percentage:.1f}%",

            x + 12,

            y + 68

        )
    # =====================================================
    # Camera Card
    # =====================================================

    def draw_camera_card(

        self,

        frame,

        camera_stats,

        x,

        y,

        width,

        height

    ):

        state = camera_stats["state"]

        if state == "CONNECTED":

            color = CAMERA_CONNECTED

        elif state == "RECOVERING":

            color = CAMERA_RECOVERING

        else:

            color = CAMERA_FAILED

        self.draw_status_card(

            frame,

            "Camera",

            state,

            color,

            x,

            y,

            width,

            height

        )
    # =====================================================
    # Confidence Card
    # =====================================================

    def draw_confidence_card(

        self,

        frame,

        confidence,

        x,

        y,

        width,

        height

    ):

        confidence = max(

            0,

            min(

                float(confidence),

                100

            )

        )

        self.draw_background(

            frame,

            x,

            y,

            width,

            height

        )

        self.draw_title(

            frame,

            "AI Confidence",

            x + 12,

            y + 24

        )

        self.draw_separator(

            frame,

            x + 10,

            y + 34,

            width - 20

        )

        self.draw_progress_bar(

            frame,

            confidence,

            x + 12,

            y + 44,

            width - 24,

            16

        )

        self.draw_label(

            frame,

            f"{confidence:.1f}%",

            x + 12,

            y + 72

        )