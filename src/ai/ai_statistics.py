"""
=========================================================
AI Statistics Engine
AI Virtual Game Controller
=========================================================

Collects gesture statistics, confidence scores,
response times, and prediction metrics.

=========================================================
"""

from collections import deque


class AIStatistics:
    """
    Tracks AI performance metrics.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(

        self,

        history_size=200

    ):

        # ---------------------------------------------
        # Session Counters
        # ---------------------------------------------

        self.total_predictions = 0

        self.valid_predictions = 0

        self.invalid_predictions = 0

        # ---------------------------------------------
        # Gesture Frequency
        # ---------------------------------------------

        self.gesture_frequency = {

            "LEFT": 0,

            "RIGHT": 0,

            "JUMP": 0,

            "SLIDE": 0,

            "PAUSE": 0

        }

        # ---------------------------------------------
        # Confidence History
        # ---------------------------------------------

        self.confidence_history = deque(

            maxlen=history_size

        )

        # ---------------------------------------------
        # Response Time History
        # ---------------------------------------------

        self.response_times = deque(

            maxlen=history_size

        )

        # ---------------------------------------------
        # Current Metrics
        # ---------------------------------------------

        self.average_confidence = 0.0

        self.average_response = 0.0

        self.accuracy = 0.0
    # =====================================================
    # Record Prediction
    # =====================================================

    def record_prediction(

        self,

        gesture,

        valid=True

    ):
        """
        Record a prediction result.
        """

        self.total_predictions += 1

        if valid:

            self.valid_predictions += 1

        else:

            self.invalid_predictions += 1

        if gesture in self.gesture_frequency:

            self.gesture_frequency[gesture] += 1

        self._update_accuracy()
    # =====================================================
    # Record Confidence
    # =====================================================

    def record_confidence(

        self,

        confidence

    ):
        """
        Store confidence score.
        """

        confidence = max(

            0,

            min(

                float(confidence),

                100

            )

        )

        self.confidence_history.append(

            confidence

        )

        self._update_average_confidence()
    # =====================================================
    # Record Response Time
    # =====================================================

    def record_response_time(

        self,

        milliseconds

    ):
        """
        Store response time.
        """

        self.response_times.append(

            float(milliseconds)

        )

        self._update_average_response()
    # =====================================================
    # Update Accuracy
    # =====================================================

    def _update_accuracy(

        self

    ):

        if self.total_predictions == 0:

            self.accuracy = 0.0

            return

        self.accuracy = (

            self.valid_predictions

            /

            self.total_predictions

        ) * 100
    # =====================================================
    # Average Confidence
    # =====================================================

    def _update_average_confidence(

        self

    ):

        if len(self.confidence_history) == 0:

            self.average_confidence = 0.0

            return

        self.average_confidence = (

            sum(

                self.confidence_history

            )

            /

            len(

                self.confidence_history

            )

        )
    # =====================================================
    # Average Response
    # =====================================================

    def _update_average_response(

        self

    ):

        if len(self.response_times) == 0:

            self.average_response = 0.0

            return

        self.average_response = (

            sum(

                self.response_times

            )

            /

            len(

                self.response_times

            )

        )
    # =====================================================
    # Most Used Gesture
    # =====================================================

    def get_most_used_gesture(self):
        """
        Return the most frequently detected gesture.
        """

        if sum(self.gesture_frequency.values()) == 0:

            return "NONE"

        return max(

            self.gesture_frequency,

            key=self.gesture_frequency.get

        )
    # =====================================================
    # Statistics
    # =====================================================

    def get_statistics(self):
        """
        Return all AI statistics.
        """

        return {

            "total_predictions": self.total_predictions,

            "valid_predictions": self.valid_predictions,

            "invalid_predictions": self.invalid_predictions,

            "accuracy": round(

                self.accuracy,

                2

            ),

            "average_confidence": round(

                self.average_confidence,

                2

            ),

            "average_response": round(

                self.average_response,

                2

            ),

            "most_used_gesture": self.get_most_used_gesture(),

            "gesture_frequency": dict(

                self.gesture_frequency

            )

        }
    # =====================================================
    # Reset
    # =====================================================

    def reset(self):
        """
        Reset session statistics.
        """

        self.total_predictions = 0

        self.valid_predictions = 0

        self.invalid_predictions = 0

        for gesture in self.gesture_frequency:

            self.gesture_frequency[gesture] = 0

        self.confidence_history.clear()

        self.response_times.clear()

        self.average_confidence = 0.0

        self.average_response = 0.0

        self.accuracy = 0.0
    # =====================================================
    # String Representation
    # =====================================================

    def __str__(self):

        return (

            f"AIStatistics("

            f"Accuracy={self.accuracy:.1f}%, "

            f"Confidence={self.average_confidence:.1f}%, "

            f"Response={self.average_response:.1f} ms, "

            f"Predictions={self.total_predictions})"

        )