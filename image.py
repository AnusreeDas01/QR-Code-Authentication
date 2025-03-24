import os

dataset_path = "dataset/"

first_print_path = os.path.join(dataset_path, "First Print")
second_print_path = os.path.join(dataset_path, "Second Print")

first_print_count = len([f for f in os.listdir(first_print_path) if f.endswith(('.png', '.jpg', '.jpeg'))])
second_print_count = len([f for f in os.listdir(second_print_path) if f.endswith(('.png', '.jpg', '.jpeg'))])

print(f"✅ First Print Images: {first_print_count}")
print(f"✅ Second Print Images: {second_print_count}")
print(f"✅ Total Images: {first_print_count + second_print_count}")  # Total