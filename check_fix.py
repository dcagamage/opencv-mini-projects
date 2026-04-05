import sys
import mediapipe as mp
import os

print(f"--- Environment Check ---")
print(f"Python Version: {sys.version}")
print(f"MediaPipe Version: {mp.__version__}")
print(f"Executable Path: {sys.executable}")

# Check if the solutions folder actually exists on your hard drive
mp_path = os.path.dirname(mp.__file__)
solutions_path = os.path.join(mp_path, "solutions")
exists = os.path.exists(solutions_path)

print(f"Solutions Folder Path: {solutions_path}")
print(f"Does folder exist?: {exists}")
print(f"mp.solutions attribute found: {hasattr(mp, 'solutions')}")