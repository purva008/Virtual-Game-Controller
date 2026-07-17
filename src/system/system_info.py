"""
=========================================================
AI Virtual Game Controller
Professional System Information Engine
=========================================================

Collects system information for the dashboard.

Features
--------
✓ Operating System
✓ Python Version
✓ OpenCV Version
✓ MediaPipe Version
✓ CPU Usage
✓ RAM Usage
✓ Total Memory
✓ Available Memory
✓ Processor
✓ Machine Architecture
✓ Hostname
✓ Username
✓ Boot Time

Author : Uttam Ahire
Version : 3.0
=========================================================
"""

import platform
import socket
import getpass
import datetime

import cv2
import mediapipe as mp
import psutil


class SystemInfo:
    """
    Collects system information for the application.
    """

    def __init__(self):

        self.info = {}

    # =====================================================
    # Operating System
    # =====================================================

    def get_os(self):

        return f"{platform.system()} {platform.release()}"

    # =====================================================
    # Python Version
    # =====================================================

    def get_python(self):

        return platform.python_version()

    # =====================================================
    # OpenCV Version
    # =====================================================

    def get_opencv(self):

        return cv2.__version__

    # =====================================================
    # MediaPipe Version
    # =====================================================

    def get_mediapipe(self):

        return mp.__version__

    # =====================================================
    # CPU Usage
    # =====================================================

    def get_cpu_usage(self):

        return psutil.cpu_percent(interval=0.1)

    # =====================================================
    # Processor Name
    # =====================================================

    def get_processor(self):

        return platform.processor()

    # =====================================================
    # RAM Information
    # =====================================================

    def get_memory(self):

        memory = psutil.virtual_memory()

        return {

            "total": round(memory.total / (1024 ** 3), 2),

            "available": round(memory.available / (1024 ** 3), 2),

            "used": round(memory.used / (1024 ** 3), 2),

            "percent": memory.percent

        }

    # =====================================================
    # Machine Type
    # =====================================================

    def get_machine(self):

        return platform.machine()

    # =====================================================
    # Host Name
    # =====================================================

    def get_hostname(self):

        return socket.gethostname()

    # =====================================================
    # Current User
    # =====================================================

    def get_username(self):

        return getpass.getuser()

    # =====================================================
    # Boot Time
    # =====================================================

    def get_boot_time(self):

        boot = datetime.datetime.fromtimestamp(

            psutil.boot_time()

        )

        return boot.strftime("%H:%M:%S")

    # =====================================================
    # Complete System Information
    # =====================================================

    def get_info(self):

        memory = self.get_memory()

        self.info = {

            "os": self.get_os(),

            "python": self.get_python(),

            "opencv": self.get_opencv(),

            "mediapipe": self.get_mediapipe(),

            "cpu": self.get_cpu_usage(),

            "ram": memory["percent"],

            "processor": self.get_processor(),

            "machine": self.get_machine(),

            "hostname": self.get_hostname(),

            "username": self.get_username(),

            "memory_total": memory["total"],

            "memory_available": memory["available"],

            "memory_used": memory["used"],

            "memory_percent": memory["percent"],

            "boot_time": self.get_boot_time()

        }
        return self.info

    # =====================================================
    # Console Report
    # =====================================================

    def print_report(self):

        info = self.get_info()

        print()

        print("=" * 60)

        print("SYSTEM INFORMATION")

        print("=" * 60)

        print(f"Operating System : {info['os']}")

        print(f"Python Version   : {info['python']}")

        print(f"OpenCV Version   : {info['opencv']}")

        print(f"MediaPipe        : {info['mediapipe']}")

        print(f"Processor        : {info['processor']}")

        print(f"Machine          : {info['machine']}")

        print(f"CPU Usage        : {info['cpu']} %")

        print(f"RAM Usage        : {info['memory_percent']} %")

        print(f"RAM Total        : {info['memory_total']} GB")

        print(f"RAM Used         : {info['memory_used']} GB")

        print(f"RAM Available    : {info['memory_available']} GB")

        print(f"Computer Name    : {info['hostname']}")

        print(f"User             : {info['username']}")

        print(f"Boot Time        : {info['boot_time']}")

        print("=" * 60)


# =========================================================
# Standalone Testing
# =========================================================

if __name__ == "__main__":

    system = SystemInfo()

    system.print_report()