import logging
import os

# ==========================================================
# Create Logs Directory
# ==========================================================

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

# ==========================================================
# Logger Configuration
# ==========================================================

logger = logging.getLogger("VirtualGameController")

logger.setLevel(logging.INFO)

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

# ==========================================================
# Helper Functions
# ==========================================================

def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_debug(message):
    logger.debug(message)