"""
=========================================================
AI Virtual Game Controller
Professional Performance Monitor
Version 3.0
=========================================================

Monitors

✓ FPS
✓ Average FPS
✓ Frame Time
✓ CPU Usage
✓ RAM Usage
✓ Runtime
✓ Frame Counter
✓ Performance Grade

Author : Uttam Ahire
=========================================================
"""

import time
import statistics
import psutil

from collections import deque


class PerformanceMonitor:
    """
    Professional Performance Monitoring Engine
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(self):

        # ----------------------------------------------
        # Application Runtime
        # ----------------------------------------------

        self.start_time = time.time()

        self.runtime = 0

        # ----------------------------------------------
        # Frame Timing
        # ----------------------------------------------

        self.previous_time = 0

        self.current_time = 0

        self.frame_time = 0

        # ----------------------------------------------
        # FPS
        # ----------------------------------------------

        self.current_fps = 0

        self.average_fps = 0

        # Keep the last 60 FPS readings
        self.fps_history = deque(maxlen=60)

        # ----------------------------------------------
        # Frame Counter
        # ----------------------------------------------

        self.frame_counter = 0

        # ----------------------------------------------
        # CPU
        # ----------------------------------------------

        self.cpu_usage = 0

        # ----------------------------------------------
        # RAM
        # ----------------------------------------------

        self.memory_usage = 0

        self.memory_available = 0

        self.memory_total = 0

        # ----------------------------------------------
        # Performance Grade
        # ----------------------------------------------

        self.performance_grade = "Excellent"

        # ----------------------------------------------
        # Internal Statistics Dictionary
        # ----------------------------------------------

        self.stats = {

            "fps": 0,

            "average_fps": 0,

            "frame_time": 0,

            "runtime": 0,

            "frame_counter": 0,

            "cpu": 0,

            "memory_percent": 0,

            "memory_available": 0,

            "memory_total": 0,

            "grade": "Excellent"

        }

    # =====================================================
    # Private
    # Determine Performance Grade
    # =====================================================

    def _calculate_grade(self):
        """
        Determines the application performance grade
        based on average FPS.
        """

        if self.average_fps >= 55:

            self.performance_grade = "Excellent"

        elif self.average_fps >= 40:

            self.performance_grade = "Good"

        elif self.average_fps >= 25:

            self.performance_grade = "Average"

        else:

            self.performance_grade = "Poor"
    # =====================================================
    # Update Performance Statistics
    # =====================================================

    def update(self):
        """
        Updates all runtime performance statistics.

        Call this once every frame.
        """

        # ----------------------------------------------
        # Frame Counter
        # ----------------------------------------------

        self.frame_counter += 1

        # ----------------------------------------------
        # Current Time
        # ----------------------------------------------

        self.current_time = time.time()

        # ----------------------------------------------
        # Runtime
        # ----------------------------------------------

        self.runtime = self.current_time - self.start_time

        # ----------------------------------------------
        # FPS
        # ----------------------------------------------

        if self.previous_time == 0:

            self.current_fps = 0

            self.frame_time = 0

        else:

            delta = self.current_time - self.previous_time

            if delta > 0:

                self.current_fps = 1 / delta

                self.frame_time = delta * 1000

            else:

                self.current_fps = 0

                self.frame_time = 0

        self.previous_time = self.current_time

        # ----------------------------------------------
        # FPS History
        # ----------------------------------------------

        if self.current_fps > 0:

            self.fps_history.append(self.current_fps)

        # ----------------------------------------------
        # Average FPS
        # ----------------------------------------------

        if len(self.fps_history) > 0:

            self.average_fps = statistics.mean(
                self.fps_history
            )

        else:

            self.average_fps = 0

        # ----------------------------------------------
        # CPU Usage
        # ----------------------------------------------

        self.cpu_usage = psutil.cpu_percent(
            interval=None
        )

        # ----------------------------------------------
        # RAM Usage
        # ----------------------------------------------

        memory = psutil.virtual_memory()

        self.memory_usage = memory.percent

        self.memory_available = (
            memory.available
            / (1024 ** 3)
        )

        self.memory_total = (
            memory.total
            / (1024 ** 3)
        )

        # ----------------------------------------------
        # Performance Grade
        # ----------------------------------------------

        self._calculate_grade()

        # ----------------------------------------------
        # Statistics Dictionary
        # ----------------------------------------------

        self.stats = {

            "fps": round(
                self.current_fps,
                2
            ),

            "average_fps": round(
                self.average_fps,
                2
            ),

            "frame_time": round(
                self.frame_time,
                2
            ),

            "runtime": round(
                self.runtime,
                2
            ),

            "frame_counter": self.frame_counter,

            "cpu": round(
                self.cpu_usage,
                1
            ),

            "memory_percent": round(
                self.memory_usage,
                1
            ),

            "memory_available": round(
                self.memory_available,
                2
            ),

            "memory_total": round(
                self.memory_total,
                2
            ),

            "grade": self.performance_grade

        }
    # =====================================================
    # Get Statistics
    # =====================================================

    def get_stats(self):
        """
        Returns the latest performance statistics.

        Returns
        -------
        dict
            Dictionary containing all monitored values.
        """

        return self.stats.copy()
    # =====================================================
    # Current FPS
    # =====================================================

    def get_fps(self):

        return self.current_fps
    # =====================================================
    # Average FPS
    # =====================================================

    def get_average_fps(self):

        return self.average_fps
    # =====================================================
    # Runtime
    # =====================================================

    def get_runtime(self):

        return self.runtime
    # =====================================================
    # Frame Time
    # =====================================================

    def get_frame_time(self):

        return self.frame_time

    # =====================================================
    # Reset Monitor
    # =====================================================

    def reset(self):
        """
        Resets the monitor to its initial state.
        """

        self.start_time = time.time()

        self.previous_time = 0

        self.current_time = 0

        self.frame_time = 0

        self.current_fps = 0

        self.average_fps = 0

        self.frame_counter = 0

        self.cpu_usage = 0

        self.memory_usage = 0

        self.memory_available = 0

        self.memory_total = 0

        self.performance_grade = "Excellent"

        self.fps_history.clear()

        self.stats = {

            "fps": 0,

            "average_fps": 0,

            "frame_time": 0,

            "runtime": 0,

            "frame_counter": 0,

            "cpu": 0,

            "memory_percent": 0,

            "memory_available": 0,

            "memory_total": 0,

            "grade": "Excellent"

        }


# =========================================================
# Standalone Testing
# =========================================================

if __name__ == "__main__":

    monitor = PerformanceMonitor()

    print("=" * 60)
    print("Performance Monitor Test")
    print("=" * 60)

    try:

        while True:

            monitor.update()

            stats = monitor.get_stats()

            print(
                f"FPS: {stats['fps']:>6} | "
                f"Avg FPS: {stats['average_fps']:>6} | "
                f"CPU: {stats['cpu']:>5}% | "
                f"RAM: {stats['memory_percent']:>5}% | "
                f"Frame: {stats['frame_counter']:>6} | "
                f"Runtime: {stats['runtime']:>8}s | "
                f"Grade: {stats['grade']}"
            )

            time.sleep(1)

    except KeyboardInterrupt:

        print("\nPerformance monitor stopped.")