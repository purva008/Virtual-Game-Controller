"""
=========================================================
AI Virtual Game Controller
Configuration File
=========================================================
"""

# =========================================================
# Camera Settings
# =========================================================

CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

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

# Number of frames used for gesture smoothing
GESTURE_HISTORY = 5

# =========================================================
# Motion Detection
# =========================================================

# Minimum hand movement (in pixels) to trigger an action
# Increase if movements are too sensitive
# Decrease if gestures are not detected easily

MOVE_THRESHOLD_X = 50

MOVE_THRESHOLD_Y = 50

# Number of frames to wait before allowing another movement
# Prevents repeated LEFT/RIGHT/JUMP/SLIDE actions

MOTION_COOLDOWN = 0.30

# =========================================================
# Mouse Control (Optional)
# =========================================================

# Used only if you later add mouse mode
MOUSE_SMOOTHING = 5

# =========================================================
# Keyboard Control
# =========================================================

# Delay between simulated key presses
KEY_PRESS_DELAY = 0.20

# =========================================================
# UI Settings
# =========================================================

FONT_SCALE = 0.8

FONT_THICKNESS = 2

TEXT_COLOR = (0, 255, 0)

INFO_COLOR = (255, 255, 0)

WARNING_COLOR = (0, 0, 255)

BOUNDING_BOX_COLOR = (255, 255, 0)

BOUNDING_BOX_THICKNESS = 2

# =========================================================
# Debug Mode
# =========================================================

# Set to True to print movement values in the terminal
DEBUG = False