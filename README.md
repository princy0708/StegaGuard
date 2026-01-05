# StegaGuard 🔍 – Universal Steganography Detection Tool

StegaGuard is an advanced **Machine Learning–based forensic tool** designed to detect steganography in **images, audio, and video files**. It analyzes real-world files, generates SHA256 hashes for integrity verification, and produces confidence-based forensic reports.

---

## 🌟 Features

- ✅ Detects steganography in **images (PNG, JPG)**  
- ✅ Detects steganography in **audio files (MP3, WAV)**  
- ✅ Detects steganography in **video files (MP4, AVI)**  
- ✅ Generates **SHA256 hash** for file integrity  
- ✅ Produces **forensic-style reports** with confidence scores  
- ✅ Designed to work on **real-world files**, not only datasets  
- ✅ Fully implemented in **Python** with ML models  

---

## 💻 Technologies Used

- Python 3.13+  
 
- Scikit-learn  
- OpenCV  
- Librosa (audio processing)  
- FFmpeg (video processing)  
- NumPy / Pandas  
- Git for version control  

---

## 📦 Installation

Follow these steps to set up **StegaGuard** locally:
1.**Clone the repository:**
git clone https://github.com/princy0708/StegaGuard.git
cd StegaGuard
2. **Create a virtual environment**
python3 -m venv venv
source venv/bin/activate   # Linux / macOS


3.**Install dependencies:**
pip install -r requirements.txt
Note: Ensure you have ffmpeg installed for video processing and librosa for audio processing. On Linux:
sudo apt update
sudo apt install ffmpeg
4.**🛠 Usage**
Run StegaGuard on any file (image, audio, video):
python3 run_stegaguard.py <file_path>
5.**⚠️ Disclaimer**

This tool is intended for educational and forensic research purposes only. Do not use it to access or manipulate files without authorization.
