"""
=========================================================
AI Core Engine
AI Virtual Game Controller
=========================================================

Central AI Pipeline

Manages:

- Gesture Smoother
- Adaptive Threshold
- AI Statistics

Future:

- Gesture Prediction
- Personalized Learning
- AI Diagnostics

=========================================================
"""

import time

from ai.gesture_smoother import GestureSmoother
from ai.adaptive_threshold import AdaptiveThreshold
from ai.ai_statistics import AIStatistics


class AICore:
    """
    Central AI Processing Engine.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(

        self,

        history_size=10,

        minimum_votes=6,

        threshold_x=35,

        threshold_y=30

    ):

        # ---------------------------------------------
        # AI Modules
        # ---------------------------------------------

        self.smoother = GestureSmoother(

            history_size=history_size,

            minimum_votes=minimum_votes

        )

        self.adaptive = AdaptiveThreshold(

            default_x=threshold_x,

            default_y=threshold_y

        )

        self.statistics = AIStatistics()

        # ---------------------------------------------
        # Current State
        # ---------------------------------------------

        self.current_gesture = "NONE"

        self.current_confidence = 0.0

        self.processing_time = 0.0

        self.last_update = time.time()
    # =====================================================
    # Process Gesture
    # =====================================================

    def process(

        self,

        gesture,

        dx,

        dy,

        confidence

    ):
        """
        Main AI processing pipeline.
        """

        start_time = time.perf_counter()

        # ---------------------------------------------
        # Adaptive Threshold
        # ---------------------------------------------

        self.adaptive.update(

            dx,

            dy

        )

        # ---------------------------------------------
        # Gesture Smoothing
        # ---------------------------------------------

        self.smoother.add(

            gesture

        )

        stable = self.smoother.get_stable_gesture()

        if stable is None:

            stable = "NONE"
        # ---------------------------------------------
        # Confidence
        # ---------------------------------------------

        if stable != "NONE":

            self.current_confidence = self.smoother.get_confidence()

        else:

            self.current_confidence = confidence

        self.statistics.record_confidence(

            self.current_confidence

        )
        # ---------------------------------------------
        # Statistics
        # ---------------------------------------------

        if stable != "NONE":

            self.statistics.record_prediction(

                stable,

                True

            )

        self.current_gesture = stable

        # ---------------------------------------------
        # Processing Time
        # ---------------------------------------------

        self.processing_time = (

            time.perf_counter()

            -

            start_time

        ) * 1000

        self.statistics.record_response_time(

            self.processing_time

        )

        return stable
    # =====================================================
    # Current Gesture
    # =====================================================

    def get_gesture(

        self

    ):

        return self.current_gesture
    # =====================================================
    # Confidence
    # =====================================================

    def get_confidence(

        self

    ):

        return self.current_confidence
    # =====================================================
    # Processing Time
    # =====================================================

    def get_processing_time(

        self

    ):

        return self.processing_time
    # =====================================================
    # Adaptive Threshold
    # =====================================================

    def get_thresholds(

        self

    ):

        return (

            self.adaptive.get_threshold_x(),

            self.adaptive.get_threshold_y()

        )
    # =====================================================
    # Threshold X
    # =====================================================

    def get_threshold_x(

        self

    ):

        return self.adaptive.get_threshold_x()
    # =====================================================
    # Threshold Y
    # =====================================================

    def get_threshold_y(

        self

    ):

        return self.adaptive.get_threshold_y()
    # =====================================================
    # AI Statistics
    # =====================================================

    def get_statistics(

        self

    ):

        return self.statistics.get_statistics()
    # =====================================================
    # Reset
    # =====================================================

    def reset(

        self

    ):

        self.smoother.reset()

        self.adaptive.reset()

        self.current_gesture = "NONE"

        self.current_confidence = 0.0

        self.processing_time = 0.0

        self.last_update = time.time()
    # =====================================================
    # String Representation
    # =====================================================

    def __str__(

        self

    ):

        return (

            f"AICore("

            f"Gesture={self.current_gesture}, "

            f"Confidence={self.current_confidence:.1f}%, "

            f"Processing={self.processing_time:.2f} ms)"

        )