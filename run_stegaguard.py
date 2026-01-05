import os
import sys
import time
from utils import detect_image, detect_audio, detect_video, get_sha256

def get_file_type(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
        return "IMAGE"
    elif ext in [".mp3", ".wav", ".flac", ".aac"]:
        return "AUDIO"
    elif ext in [".mp4", ".avi", ".mov", ".mkv", ".webm"]:
        return "VIDEO"
    else:
        return "UNKNOWN"

def main():
    # Use command-line argument if provided
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter file path: ").strip()

    if not os.path.exists(file_path):
        print("File does not exist:", file_path)
        return

    start_time = time.time()
    file_type = get_file_type(file_path)
    sha256 = get_sha256(file_path)

    if file_type == "IMAGE":
        verdict, confidence = detect_image(file_path)
    elif file_type == "AUDIO":
        verdict, confidence = detect_audio(file_path)
    elif file_type == "VIDEO":
        verdict, confidence = detect_video(file_path)
    else:
        verdict, confidence = "ERROR", 0

    end_time = time.time()

    print("\nStegaGuard v5.0 – Universal Steganalysis Report")
    print("-" * 50)
    print(f"File: {file_path}")
    print(f"Type: {file_type}")
    print(f"SHA256: {sha256}")
    print(f"\nVerdict: {verdict}")
    print(f"Confidence: {confidence}%")
    print(f"Time: {time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")

if __name__ == "__main__":
    main()
