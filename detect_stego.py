import hashlib
import joblib
import os
import sys
from datetime import datetime
from feature_extractor import extract_features
from cnn_predict import cnn_predict

ML_MODEL = joblib.load("stegaguard_model.pkl")

def sha256(file):
    h = hashlib.sha256()
    with open(file, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def detect(image_path):
    features = extract_features(image_path)
    ml_pred = ML_MODEL.predict([features])[0]
    ml_prob = max(ML_MODEL.predict_proba([features])[0])
    cnn_prob = cnn_predict(image_path)

    if ml_pred == 1 and cnn_prob > 0.6:
        verdict = "STEGO CONFIRMED"
    elif cnn_prob > 0.8:
        verdict = "STEGO (Advanced)"
    else:
        verdict = "CLEAN"

    report = f"""
StegaGuard v3.0 Forensic Report
--------------------------------
Image: {image_path}
SHA256: {sha256(image_path)}

ML Verdict: {'STEGO' if ml_pred==1 else 'CLEAN'}
ML Confidence: {ml_prob*100:.2f}%

CNN Confidence: {cnn_prob*100:.2f}%
Final Verdict: {verdict}
Time: {datetime.now()}
"""
    os.makedirs("reports", exist_ok=True)
    fname = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(fname, "w") as f:
        f.write(report)

    print(report)
    print(f"[+] Report saved as {fname}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 detect_stego.py <image_path_or_folder>")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isdir(path):
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                detect(full_path)
    elif os.path.isfile(path):
        detect(path)
    else:
        print("[!] Invalid path")
