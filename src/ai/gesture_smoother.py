"""
=========================================================
AI Virtual Game Controller
Gesture Smoother Engine
=========================================================

Stabilizes gesture recognition by filtering noisy
predictions across multiple frames.

Features
--------
✓ Gesture History Buffer
✓ Majority Voting
✓ Confidence Calculation
✓ Adaptive Smoothing
✓ Statistics

Author : Uttam Ahire
Version : 2.0
=========================================================
"""

from collections import deque
from collections import Counter


class GestureSmoother:
    """
    Professional gesture smoothing engine.

    Stores recent gesture predictions and
    outputs the most stable gesture.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(

        self,

        history_size=10,

        minimum_votes=6

    ):

        # Number of frames stored
        self.history_size = history_size

        # Minimum votes required
        self.minimum_votes = minimum_votes

        # Gesture history buffer
        self.history = deque(

            maxlen=self.history_size

        )

        # Current stable gesture
        self.current_gesture = None

        # Current confidence
        self.current_confidence = 0.0

        # Statistics
        self.total_frames = 0

        self.valid_frames = 0

        self.statistics = {

            "gesture_changes": 0,

            "stable_predictions": 0,

            "ignored_predictions": 0

        }

    # =====================================================
    # Add Gesture
    # =====================================================

    def add(

        self,

        gesture

    ):
        """
        Add gesture into history buffer.
        """

        if gesture is None:

            return

        self.total_frames += 1

        self.history.append(

            gesture

        )

    # =====================================================
    # Update
    # =====================================================

    def update(

        self,

        gesture

    ):
        """
        Add a gesture and immediately
        return the stable gesture.
        """

        self.add(

            gesture

        )

        return self.get_stable_gesture()

    # =====================================================
    # Change History Size
    # =====================================================

    def set_history_size(

        self,

        history_size

    ):

        history_size = max(

            3,

            int(history_size)

        )

        self.history_size = history_size

        self.history = deque(

            self.history,

            maxlen=self.history_size

        )

    # =====================================================
    # Minimum Votes
    # =====================================================

    def set_minimum_votes(

        self,

        minimum_votes

    ):

        self.minimum_votes = max(

            1,

            int(minimum_votes)

        )

    # =====================================================
    # Reset
    # =====================================================

    def reset(self):
        """
        Reset complete smoothing engine.
        """

        self.history = deque(

            maxlen=self.history_size

        )

        self.current_gesture = None

        self.current_confidence = 0.0

        self.total_frames = 0

        self.valid_frames = 0

        self.statistics = {

            "gesture_changes": 0,

            "stable_predictions": 0,

            "ignored_predictions": 0

        }
    # =====================================================
    # Analyze History
    # =====================================================

    def analyze(self):
        """
        Analyze current gesture history.

        Returns
        -------
        (gesture, confidence)
        """

        if len(self.history) == 0:

            return None, 0.0

        counter = Counter(self.history)

        gesture, votes = counter.most_common(1)[0]

        confidence = (

            votes /

            len(self.history)

        ) * 100

        return gesture, confidence

    # =====================================================
    # Stable Gesture
    # =====================================================

    def get_stable_gesture(self):
        """
        Return the most stable gesture.
        """

        if len(self.history) < self.minimum_votes:

            self.current_confidence = 0.0

            return None

        gesture, confidence = self.analyze()

        required = (

            self.minimum_votes /

            len(self.history)

        ) * 100

        if confidence >= required:

            if gesture != self.current_gesture:

                self.statistics["gesture_changes"] += 1

            self.current_gesture = gesture

            self.current_confidence = confidence

            self.valid_frames += 1

            self.statistics["stable_predictions"] += 1

            return gesture

        self.statistics["ignored_predictions"] += 1

        self.current_confidence = confidence

        return None

    # =====================================================
    # Confidence
    # =====================================================

    def get_confidence(self):
        """
        Return confidence of current gesture.
        """

        return round(

            self.current_confidence,

            2

        )

    # =====================================================
    # Current Gesture
    # =====================================================

    def get_current_gesture(self):
        """
        Return current stable gesture.
        """

        return self.current_gesture

    # =====================================================
    # Gesture History
    # =====================================================

    def get_history(self):
        """
        Return gesture history.
        """

        return list(

            self.history

        )

    # =====================================================
    # Buffer Size
    # =====================================================

    def buffer_size(self):
        """
        Return current history size.
        """

        return len(

            self.history

        )

    # =====================================================
    # Statistics
    # =====================================================

    def get_statistics(self):
        """
        Return smoothing statistics.
        """

        stats = self.statistics.copy()

        stats["total_frames"] = self.total_frames

        stats["valid_frames"] = self.valid_frames

        stats["buffer_size"] = len(

            self.history

        )

        stats["current_gesture"] = self.current_gesture

        stats["confidence"] = round(

            self.current_confidence,

            2

        )

        return stats

    # =====================================================
    # String Representation
    # =====================================================

    def __str__(self):

        return (

            f"GestureSmoother("

            f"Gesture={self.current_gesture}, "

            f"Confidence={self.current_confidence:.1f}%, "

            f"Frames={self.total_frames})"

        )
    # =====================================================
    # Standalone Testing
    # =====================================================

    if __name__ == "__main__":

        print("=" * 60)
        print(" Gesture Smoother Engine Test")
        print("=" * 60)

        smoother = GestureSmoother(

            history_size=10,

            minimum_votes=6

        )

        test_sequence = [

            "RIGHT",
            "RIGHT",
            "RIGHT",
            "LEFT",
            "RIGHT",
            "RIGHT",
            "RIGHT",
            "RIGHT",
            "LEFT",
            "RIGHT",
            "RIGHT",
            "RIGHT"

        ]

        print("\nFrame-by-Frame Results\n")

        for frame, gesture in enumerate(test_sequence, start=1):

            stable = smoother.update(gesture)

            print(

                f"Frame {frame:02d}"

                f" | Input : {gesture:>5}"

                f" | Stable : {str(stable):>5}"

                f" | Confidence : {smoother.get_confidence():6.2f}%"

            )

        print("\n")

        print("=" * 60)
        print("History")
        print("=" * 60)

        print(

            smoother.get_history()

        )

        print()

        print("=" * 60)
        print("Statistics")
        print("=" * 60)

        stats = smoother.get_statistics()

        for key, value in stats.items():

            print(

                f"{key:20}: {value}"

            )

        print()

        print("=" * 60)
        print("Current Gesture")
        print("=" * 60)

        print(

            smoother.get_current_gesture()

        )

        print()

        print("=" * 60)
        print("Object")
        print("=" * 60)

        print(

            smoother

        )

        print()

        print("=" * 60)
        print("Gesture Smoother Test Completed Successfully")
        print("=" * 60)
            