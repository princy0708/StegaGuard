import cv2
import numpy as np

def detect_video_stego(video_path):
    cap = cv2.VideoCapture(video_path)
    variances = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        variances.append(np.var(gray))

    cap.release()

    if len(variances) < 10:
        return None, "Video too short"

    variance_std = np.std(variances)

    if variance_std > 500:
        return True, round(variance_std, 2)
    else:
        return False, round(variance_std, 2)
