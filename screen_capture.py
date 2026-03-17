import cv2
import numpy as np
import mss

def take_screenshot():
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[2])  # Adjust the monitor index if needed
        image = np.array(screenshot)
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        return image