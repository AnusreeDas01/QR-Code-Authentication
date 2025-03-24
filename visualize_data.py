import matplotlib.pyplot as plt
import cv2
import os

dataset_path = "dataset/"

first_print_path = os.path.join(dataset_path, "First Print")
second_print_path = os.path.join(dataset_path, "Second Print")

# List sample images
first_print_images = os.listdir(first_print_path)[:5]
second_print_images = os.listdir(second_print_path)[:5]

fig, axes = plt.subplots(2, 5, figsize=(15, 6))

# Display First Print images
for i, img_name in enumerate(first_print_images):
    img = cv2.imread(os.path.join(first_print_path, img_name), cv2.IMREAD_GRAYSCALE)
    axes[0, i].imshow(img, cmap='gray')
    axes[0, i].set_title("First Print")
    axes[0, i].axis("off")

# Display Second Print images
for i, img_name in enumerate(second_print_images):
    img = cv2.imread(os.path.join(second_print_path, img_name), cv2.IMREAD_GRAYSCALE)
    axes[1, i].imshow(img, cmap='gray')
    axes[1, i].set_title("Second Print")
    axes[1, i].axis("off")

plt.show()

# Count images in each class
num_first_print = len(os.listdir(first_print_path))
num_second_print = len(os.listdir(second_print_path))

print(f"✅ First Print Images: {num_first_print}")
print(f"✅ Second Print Images: {num_second_print}")
