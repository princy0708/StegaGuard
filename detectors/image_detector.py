import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from features import extract_features

DATASET = "dataset"
X, y = [], []

for label, cls in enumerate(["clean", "stego"]):
    folder = os.path.join(DATASET, cls)
    for img in os.listdir(folder):
        path = os.path.join(folder, img)
        try:
            feats = extract_features(path)
            X.append(feats)
            y.append(label)
        except:
            pass

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

acc = model.score(X_test, y_test) * 100
print(f"[+] ML Model Accuracy: {acc:.2f}%")

joblib.dump(model, "stegaguard_model.pkl")
print("[+] Model saved as stegaguard_model.pkl")
