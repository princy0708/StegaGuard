import wave
import numpy as np
from scipy.stats import entropy

def detect_audio_stego(audio_path):
    try:
        with wave.open(audio_path, 'rb') as wf:
            frames = wf.readframes(wf.getnframes())
            samples = np.frombuffer(frames, dtype=np.int16)

        lsb = samples & 1
        lsb_entropy = entropy(np.bincount(lsb))

        if lsb_entropy > 0.9:
            return True, round(lsb_entropy * 100, 2)
        else:
            return False, round(lsb_entropy * 100, 2)

    except Exception as e:
        return None, f"Error: {str(e)}"
