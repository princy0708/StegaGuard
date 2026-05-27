# StegaGuard 🔍
### Universal Steganography Detection Tool

> *Detect what the naked eye can't see.*

StegaGuard is an advanced **ML-based forensic tool** that detects hidden data concealed within images, audio, and video files. It generates SHA256 integrity hashes and produces confidence-based forensic reports — built for real-world files, not just controlled datasets.

---

## Features

| Capability | Details |
|---|---|
| 🖼️ Image Analysis | PNG, JPG — pixel-level steganalysis |
| 🎵 Audio Analysis | MP3, WAV — spectral feature extraction |
| 🎬 Video Analysis | MP4, AVI — frame-by-frame detection |
| 🔐 Hash Verification | SHA256 integrity check on every file |
| 📄 Forensic Reports | Confidence scores + detection summary |
| 🌍 Real-World Ready | Works on uncontrolled, live files |

---

## How It Works

```
Input File (image / audio / video)
        ↓
Feature Extraction
(pixel stats / spectral analysis / frame sampling)
        ↓
ML Classification Model
        ↓
Confidence Score + SHA256 Hash
        ↓
Forensic Report Output
```

---

## Tech Stack

```txt
Language    : Python 3.13+
ML          : Scikit-learn
Vision      : OpenCV
Audio       : Librosa
Video       : FFmpeg
Data        : NumPy · Pandas
Version Ctrl: Git
```

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/princy0708/StegaGuard.git
cd StegaGuard
```

**2. Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Install system dependencies**
```bash
# FFmpeg (required for video processing)
sudo apt update && sudo apt install ffmpeg

# Verify installation
ffmpeg -version
```

---

## Usage

```bash
python3 run_stegaguard.py <file_path>
```

**Examples:**
```bash
# Analyze an image
python3 run_stegaguard.py sample.png

# Analyze an audio file
python3 run_stegaguard.py recording.wav

# Analyze a video
python3 run_stegaguard.py clip.mp4
```

**Sample output:**
```
[StegaGuard] Analyzing: sample.png
[✓] SHA256: 3a1f9c2e...
[✓] Feature extraction complete
[!] Steganography DETECTED — Confidence: 91.4%
[✓] Forensic report saved: report_sample.txt
```

---

## Project Structure

```
StegaGuard/
├── run_stegaguard.py      # Main entry point
├── models/                # Trained ML models
├── detectors/             # Image, audio, video modules
├── reports/               # Generated forensic reports
├── requirements.txt
└── README.md
```

---

## Use Cases

- 🔍 Digital forensics investigations
- 🛡️ Malware C2 payload detection
- 🎓 Cybersecurity research & CTF challenges
- 🏛️ Law enforcement evidence analysis

---

## ⚠️ Disclaimer

This tool is intended for **educational and forensic research purposes only.**
Do not use StegaGuard to access or analyze files without proper authorization.
The author is not responsible for any misuse of this tool.

---

## Author

**Princy Chauhan**
[GitHub](https://github.com/princy0708) · [LinkedIn](https://linkedin.com/in/princy-chauhan-065236373)
