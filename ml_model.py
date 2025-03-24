import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

dataset_path = "dataset/"

first_print_path = os.path.join(dataset_path, "First Print")
second_print_path = os.path.join(dataset_path, "Second Print")

def extract_features(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))
    return img.flatten()  # Convert image to 1D array

X = []
y = []

# Load First Print images (label 0)
for img_name in os.listdir(first_print_path):
    X.append(extract_features(os.path.join(first_print_path, img_name)))
    y.append(0)

# Load Second Print images (label 1)
for img_name in os.listdir(second_print_path):
    X.append(extract_features(os.path.join(second_print_path, img_name)))
    y.append(1)

X = np.array(X)
y = np.array(y)

# Split data into train & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an SVM model
svm_model = SVC(kernel="linear")
svm_model.fit(X_train, y_train)

# Train a Random Forest model
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Test models
y_pred_svm = svm_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)

print(f"🎯 SVM Accuracy: {accuracy_score(y_test, y_pred_svm) * 100:.2f}%")
print(f"🎯 Random Forest Accuracy: {accuracy_score(y_test, y_pred_rf) * 100:.2f}%")
