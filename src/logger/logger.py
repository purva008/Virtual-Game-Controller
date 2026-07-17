"""
=========================================================
AI Virtual Game Controller
Professional Logger Engine
Version 1.0
=========================================================

Features

✓ Daily Log Files
✓ Timestamped Messages
✓ INFO
✓ WARNING
✓ ERROR
✓ ACTION
✓ SYSTEM
✓ Console + File Logging
✓ UTF-8 Support

Author : Uttam Ahire
=========================================================
"""

import os
import datetime


class Logger:
    """
    Professional Application Logger

    Creates a log file for every application session and
    writes all events to both the console and the log file.
    """

    # =====================================================
    # Constructor
    # =====================================================

    def __init__(self):

        # ----------------------------------------------
        # Project Root
        # ----------------------------------------------

        self.project_root = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                ".."
            )
        )

        # ----------------------------------------------
        # Logs Folder
        # ----------------------------------------------

        self.logs_folder = os.path.join(
            self.project_root,
            "logs"
        )

        os.makedirs(
            self.logs_folder,
            exist_ok=True
        )

        # ----------------------------------------------
        # Timestamp
        # ----------------------------------------------

        self.session_time = datetime.datetime.now()

        # ----------------------------------------------
        # Log File Name
        # ----------------------------------------------

        filename = self.session_time.strftime(
            "%Y-%m-%d_%H-%M-%S.log"
        )

        self.log_file = os.path.join(
            self.logs_folder,
            filename
        )

        # ----------------------------------------------
        # Open File
        # ----------------------------------------------

        self.file = open(

            self.log_file,

            "a",

            encoding="utf-8"

        )

        # ----------------------------------------------
        # Session Header
        # ----------------------------------------------

        self._write_header()
    # =====================================================
    # Current Timestamp
    # =====================================================

    def _timestamp(self):

        return datetime.datetime.now().strftime(
            "%H:%M:%S"
        )
    # =====================================================
    # Session Header
    # =====================================================

    def _write_header(self):

        self.file.write(
            "\n"
            + "=" * 70
            + "\n"
        )

        self.file.write(
            "AI Virtual Game Controller\n"
        )

        self.file.write(
            "Professional Log Session\n"
        )

        self.file.write(
            f"Started : {self.session_time}\n"
        )

        self.file.write(
            "=" * 70
            + "\n\n"
        )

        self.file.flush()

        print("=" * 70)

        print("Logger Initialized")

        print(f"Log File : {self.log_file}")

        print("=" * 70)
    # =====================================================
    # Core Log Writer
    # =====================================================

    def _write(self, level, message):
        """
        Internal logging function.

        Parameters
        ----------
        level : str
            Log level (INFO, WARNING, ERROR, ACTION, SYSTEM)

        message : str
            Log message
        """

        timestamp = self._timestamp()

        log_line = f"[{timestamp}] [{level}] {message}"

        # Print to terminal
        print(log_line)

        # Save to log file
        self.file.write(log_line + "\n")

        self.file.flush()
    # =====================================================
    # INFO
    # =====================================================

    def info(self, message):
        """
        General information.
        """

        self._write(
            "INFO",
            message
        )
    # =====================================================
    # SYSTEM
    # =====================================================

    def system(self, message):
        """
        System events.
        """

        self._write(
            "SYSTEM",
            message
        )
    # =====================================================
    # ACTION
    # =====================================================

    def action(self, message):
        """
        Gesture/Game actions.
        """

        self._write(
            "ACTION",
            message
        )
    # =====================================================
    # WARNING
    # =====================================================

    def warning(self, message):
        """
        Warning messages.
        """

        self._write(
            "WARNING",
            message
        )
    # =====================================================
    # ERROR
    # =====================================================

    def error(self, message):
        """
        Error messages.
        """

        self._write(
            "ERROR",
            message
        )
    # =====================================================
    # SUCCESS
    # =====================================================

    def success(self, message):
        """
        Successful operations.
        """

        self._write(
            "SUCCESS",
            message
        )
    # =====================================================
    # DEBUG
    # =====================================================

    def debug(self, message):
        """
        Debug messages.
        """

        self._write(
            "DEBUG",
            message
        )
    # =====================================================
    # Session Footer
    # =====================================================

    def _write_footer(self):
        """
        Writes the session ending information.
        """

        end_time = datetime.datetime.now()

        duration = end_time - self.session_time

        self.file.write("\n")
        self.file.write("=" * 70 + "\n")
        self.file.write("Application Closed\n")
        self.file.write(f"Ended    : {end_time}\n")
        self.file.write(f"Duration : {duration}\n")
        self.file.write("=" * 70 + "\n")

        self.file.flush()
    # =====================================================
    # Close Logger
    # =====================================================

    def close(self):
        """
        Safely closes the logger.

        Writes the session footer before
        closing the log file.
        """

        try:

            self.info("Closing Logger")

            self._write_footer()

            if hasattr(self, "file") and self.file is not None:

                if not self.file.closed:

                    self.file.flush()

                    self.file.close()

        except Exception as error:

            print(f"[Logger] Error while closing logger: {error}")