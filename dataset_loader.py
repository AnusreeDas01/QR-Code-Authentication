import torch
from torch.utils.data import Dataset
import cv2
import os
import numpy as np

class QRDataset(Dataset):
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

        # ✅ Load images from BOTH subfolders
        first_print_path = os.path.join(dataset_path, "First Print")
        second_print_path = os.path.join(dataset_path, "Second Print")

        self.image_files = [
            os.path.join(first_print_path, f) for f in os.listdir(first_print_path) if f.endswith(('.png', '.jpg', '.jpeg'))
        ] + [
            os.path.join(second_print_path, f) for f in os.listdir(second_print_path) if f.endswith(('.png', '.jpg', '.jpeg'))
        ]

        if len(self.image_files) == 0:
            raise ValueError("❌ ERROR: No valid image files found in dataset!")

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        image_path = self.image_files[idx]

        print(f"📥 Loading image: {image_path}")  # Debugging

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"❌ ERROR: Could not load image {image_path}")
            return None, None  # Skip bad images

        img = cv2.resize(img, (128, 128))
        img = np.expand_dims(img, axis=0)

        img_tensor = torch.tensor(img, dtype=torch.float32) / 255.0  
        label = 1 if "Second Print" in image_path else 0
        label_tensor = torch.tensor(label, dtype=torch.float32)

        return img_tensor, label_tensor
