"""
=========================================================
AI Virtual Game Controller
Configuration File
Version 2.0 (Professional UI)
=========================================================
"""

# =========================================================
# Camera Settings
# =========================================================

CAMERA_INDEX = 0
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

WINDOW_NAME = "AI Virtual Game Controller"

# =========================================================
# MediaPipe Hand Detection
# =========================================================

MAX_HANDS = 1

DETECTION_CONFIDENCE = 0.80
TRACKING_CONFIDENCE = 0.80

# =========================================================
# Gesture Detection
# =========================================================

GESTURE_HISTORY = 5

# =========================================================
# Motion Detection
# =========================================================

MOVE_THRESHOLD_X = 50
MOVE_THRESHOLD_Y = 50

MOTION_COOLDOWN = 0.30

# =========================================================
# Mouse Settings (Reserved)
# =========================================================

MOUSE_SMOOTHING = 5

# =========================================================
# Keyboard
# =========================================================

KEY_PRESS_DELAY = 0.20

# =========================================================
# Dashboard Layout
# =========================================================

PANEL_WIDTH = 340

PADDING = 20

SECTION_SPACING = 45

# =========================================================
# Fonts
# =========================================================

FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX

TITLE_SCALE = 1.0
HEADER_SCALE = 0.8
TEXT_SCALE = 0.65
SMALL_SCALE = 0.55

TITLE_THICKNESS = 3
HEADER_THICKNESS = 2
TEXT_THICKNESS = 2

# =========================================================
# Professional Color Theme
# =========================================================

# Background
BACKGROUND_COLOR = (30, 30, 30)

# Left information panel
PANEL_COLOR = (45, 45, 45)

# Borders
BORDER_COLOR = (90, 90, 90)

# Title
TITLE_COLOR = (255, 220, 0)

# Labels
LABEL_COLOR = (220, 220, 220)

# Values
VALUE_COLOR = (0, 255, 255)

# Success
SUCCESS_COLOR = (0, 255, 0)

# Warning
WARNING_COLOR = (0, 180, 255)

# Error
ERROR_COLOR = (0, 0, 255)

# FPS
FPS_COLOR = (255, 255, 0)

# Runtime
RUNTIME_COLOR = (255, 180, 0)

# Motion Arrow
ARROW_COLOR = (255, 100, 0)

# Bounding Box
BOUNDING_BOX_COLOR = (0, 255, 255)

BOUNDING_BOX_THICKNESS = 2

# Hand Center
HAND_CENTER_COLOR = (0, 0, 255)

# =========================================================
# Status Indicators
# =========================================================

STATUS_CONNECTED = (0, 255, 0)

STATUS_WAITING = (0, 255, 255)

STATUS_DISCONNECTED = (0, 0, 255)

# =========================================================
# Action History
# =========================================================

MAX_HISTORY = 5

# =========================================================
# Motion Trail
# =========================================================

DRAW_HAND_CENTER = True

DRAW_TRAIL = True

TRAIL_LENGTH = 20

# =========================================================
# Runtime Statistics
# =========================================================

SHOW_RUNTIME = True

SHOW_FPS = True

SHOW_ACTION_COUNTER = True

SHOW_CLOCK = True

# =========================================================
# Splash Screen
# =========================================================

SHOW_SPLASH = True

SPLASH_DURATION = 2

# =========================================================
# Logging
# =========================================================

ENABLE_LOGGING = True

# =========================================================
# Debug
# =========================================================

DEBUG = False
# =========================================================
# Application
# =========================================================

APP_NAME = "AI Virtual Game Controller"

APP_VERSION = "2.0"

APP_SUBTITLE = "Motion-Based Temple Run Controller"

DEVELOPER_NAME = "Uttam Ahire"

SPLASH_DURATION = 3000  # milliseconds