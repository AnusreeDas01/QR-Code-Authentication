
import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader
from dataset_loader import QRDataset
from model import QRCodeClassifier

# Set dataset path
dataset_path = "dataset/" # Change this to your actual dataset path

# Load dataset
dataset = QRDataset(dataset_path)

# Split into training & testing sets (80% train, 20% test)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

# Create dataloaders
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)

# Initialize model, loss function, and optimizer
model = QRCodeClassifier()
criterion = nn.BCELoss()  # Binary cross-entropy loss
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    total_loss = 0.0
    for images, labels in train_loader:
        if images is None or labels is None:
            print("⚠ Skipping empty batch...")
            continue  # Skip missing images

        labels = labels.view(-1, 1)  # Reshape labels for BCE Loss

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"✅ Epoch [{epoch+1}/{num_epochs}] - Loss: {total_loss:.4f}")

# Save trained model in the 'models/' folder
torch.save(model.state_dict(), "models/qr_classifier_final.pth")
print("✅ Final model saved successfully in models/qr_classifier_final.pth")