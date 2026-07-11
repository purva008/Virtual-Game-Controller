import cv2


def draw_dashboard(frame, fps, action, hand_detected, session_time):

    height, width, _ = frame.shape

    # Create transparent overlay
    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (0, 0),
        (width, 100),
        (35, 35, 35),
        -1
    )

    alpha = 0.75
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    # Project Title
    cv2.putText(
        frame,
        "Virtual Game Controller",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )

    # FPS
    cv2.putText(
        frame,
        f"FPS : {fps}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    # Session Timer
    cv2.putText(
        frame,
        f"Session : {session_time}",
        (20, 85),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # Current Gesture
    cv2.putText(
        frame,
        f"Gesture : {action}",
        (250, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # Hand Status
    if hand_detected:
        status = "Hand Detected"
        color = (0, 255, 0)
    else:
        status = "No Hand"
        color = (0, 0, 255)

    cv2.putText(
        frame,
        status,
        (250, 85),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2
    )

    # Status Indicator
    cv2.circle(
        frame,
        (width - 30, 30),
        10,
        color,
        -1
    )

    return frame