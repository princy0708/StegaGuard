import os
import hashlib
from PIL import Image
import numpy as np
import cv2
import librosa

# ----------------------------
# Utility Functions
# ----------------------------

def get_sha256(file_path):
    """Compute SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# ----------------------------
# IMAGE STEGANOGRAPHY DETECTION
# ----------------------------

def detect_image(file_path):
    """Detect steganography in an image using simple heuristics."""
    try:
        img = Image.open(file_path)
        img_arr = np.array(img)

        # Simple LSB analysis: check least significant bit variance
        lsb = img_arr & 1
        variance = np.var(lsb)
        # heuristic threshold, adjust based on experiments
        threshold = 0.0015
        if variance > threshold:
            verdict = "STEGO"
            confidence = round(min(variance*1000, 99.99), 2)
        else:
            verdict = "CLEAN"
            confidence = round((1 - variance/threshold)*100, 2)
        return verdict, confidence
    except Exception as e:
        return "ERROR", 0

# ----------------------------
# AUDIO STEGANOGRAPHY DETECTION
# ----------------------------

def detect_audio(file_path):
    """Detect steganography in audio using basic entropy analysis."""
    try:
        y, sr = librosa.load(file_path, sr=None, mono=True)
        entropy = -np.sum(y*np.log1p(np.abs(y))) / len(y)
        threshold = 0.1
        if entropy > threshold:
            verdict = "STEGO"
            confidence = round(min(entropy*1000, 99.99), 2)
        else:
            verdict = "CLEAN"
            confidence = round((1 - entropy/threshold)*100, 2)
        return verdict, confidence
    except Exception as e:
        return "ERROR", 0

# ----------------------------
# VIDEO STEGANOGRAPHY DETECTION
# ----------------------------

def detect_video(file_path):
    """Detect steganography in video by analyzing frame LSB variance."""
    try:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            return "ERROR", 0
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        lsb_variances = []
        for i in range(0, frame_count, max(1, frame_count // 10)):  # sample 10 frames
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if not ret:
                continue
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            lsb = frame_gray & 1
            lsb_variances.append(np.var(lsb))
        cap.release()
        if not lsb_variances:
            return "ERROR", 0
        avg_variance = np.mean(lsb_variances)
        threshold = 0.0015
        if avg_variance > threshold:
            verdict = "STEGO"
            confidence = round(min(avg_variance*1000, 99.99), 2)
        else:
            verdict = "CLEAN"
            confidence = round((1 - avg_variance/threshold)*100, 2)
        return verdict, confidence
    except Exception as e:
        return "ERROR", 0

