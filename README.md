# StegaGuard 🔐

StegaGuard is an experimental machine-learning–based steganography detection tool
for **images, audio, and video files**.

## Features
- Detects possible steganography in:
  - Images (PNG, JPG)
  - Audio (WAV, MP3)
  - Video (MP4)
- Uses ML-based statistical analysis
- Generates forensic reports with SHA256 hashing
- CLI-based security tool

## Usage
```bash
python3 run_stegaguard.py <file_path>
