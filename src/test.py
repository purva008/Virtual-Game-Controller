import mediapipe as mp

print("MediaPipe version:", getattr(mp, "__version__", "Unknown"))
print("MediaPipe location:", mp.__file__)

print(dir(mp))