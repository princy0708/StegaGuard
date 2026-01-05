import cv2
import numpy as np

def lsb_ratio(gray):
    lsb = gray & 1
    return np.mean(lsb)

def entropy(gray):
    hist = np.histogram(gray, bins=256)[0]
    hist = hist / np.sum(hist)
    hist = hist[hist > 0]
    return -np.sum(hist * np.log2(hist))

def histogram_std(img):
    feats = []
    for i in range(3):
        hist = cv2.calcHist([img], [i], None, [256], [0,256])
        feats.append(np.std(hist))
    return feats

def pixel_correlation(img):
    ch = img[:,:,0]
    return np.corrcoef(ch[:-1,:].flatten(), ch[1:,:].flatten())[0,1]

def extract_features(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256,256))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    features = [
        lsb_ratio(gray),
        entropy(gray),
        pixel_correlation(img)
    ]
    features.extend(histogram_std(img))

    return features
