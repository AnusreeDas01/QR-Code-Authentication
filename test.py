import torch
from torch.utils.data import DataLoader
from dataset_loader import QRDataset
from model import QRCodeClassifier
from sklearn.metrics import confusion_matrix, classification_report

# ✅ Set dataset path
dataset_path = "dataset/"

# ✅ Load the dataset
test_dataset = QRDataset(dataset_path)
test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

# ✅ Load trained model
model = QRCodeClassifier()
model.load_state_dict(torch.load("models/qr_code_model.pth"))  # Ensure correct model path
model.eval()  # Set model to evaluation mode

# ✅ Evaluate the model
y_true = []
y_pred = []

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        predicted = (outputs.squeeze(0) > 0.5).float().item()

        y_true.append(labels.item())
        y_pred.append(predicted)

# ✅ Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# ✅ Print classification report
print("Classification Report:")
print(classification_report(y_true, y_pred))

# Load the final trained model
model.load_state_dict(torch.load("models/qr_classifier_final.pth"))
model.eval()
print("✅ Final model loaded successfully!")
