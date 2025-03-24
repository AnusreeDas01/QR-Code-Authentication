# QR Code Authentication using Machine Learning

## 📌 Project Overview
This project implements **QR Code Authentication** using **Deep Learning (CNNs)** and **Traditional Machine Learning (SVM, Random Forest)** to classify QR codes as **Original (First Print)** or **Counterfeit (Second Print)**.

🚀 **Key Features:**
- **CNN-based Model** for high-accuracy classification.
- **SVM & Random Forest Models** for comparison.
- **Automated Dataset Preprocessing**.
- **Confusion Matrix & Model Evaluation Metrics**.
- **Deployment Considerations** for real-world applications.

---
## 📂 Project Structure
```
QR_Auth_Project/
│── dataset/               # Folder containing QR code images
│   │── First Print/       # Original QR codes
│   │── Second Print/      # Counterfeit QR codes
│── models/                # Folder to save trained models
│   │── qr_classifier_final.pth  # ✅ Final trained CNN model
│── dataset_loader.py      # Custom PyTorch dataset class
│── model.py               # CNN model definition
│── train.py               # CNN training script
│── test.py                # CNN evaluation script
│── ml_model.py            # Traditional ML model (SVM/Random Forest)
│── visualize_data.py      # Data visualization & statistics
│── requirements.txt       # Dependencies list
│── README.md              # This file (Project Documentation)
│── report.docx            # Final report for submission
```
---
## 🔧 Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/AnusreeDas01/QR-Code-Authentication.git
cd QR-Code-Authentication
```
### 2️⃣ **Install Dependencies**
Make sure you have **Python 3.8+** installed. Then install the required libraries:
```bash
pip install -r requirements.txt
```
If using **Git LFS** (for large files like models), install it:
```bash
git lfs install
```

---
## 🚀 How to Run the Project
### 1️⃣ **Data Visualization & Analysis**
```bash
python visualize_data.py
```
🔹 This will display **sample images** and dataset statistics.

### 2️⃣ **Train the CNN Model**
```bash
python train.py
```
🔹 This will train the **CNN model** and save it as `models/qr_classifier_final.pth`.

### 3️⃣ **Evaluate the CNN Model**
```bash
python test.py
```
🔹 This will print the **confusion matrix & classification report**.

### 4️⃣ **Train Traditional ML Models (SVM & Random Forest)**
```bash
python ml_model.py
```
🔹 This will train and evaluate **SVM & Random Forest models**.

### 5️⃣ **Push the Project to GitHub**
If you face issues pushing large files, use Git LFS:
```bash
git lfs track "*.pth"
git add .
git commit -m "Added trained model"
git push origin main
```

---
## 📊 Model Performance
| Model  | Accuracy |
|--------|----------|
| **CNN**    | 100.00%  |
| **SVM**    | 100.00%  |
| **Random Forest** | 97.50%  |

### ✅ **Confusion Matrix**
| Actual | Predicted First Print | Predicted Second Print |
|--------|-----------------|------------------|
| First Print  | 100  | 0 |
| Second Print | 0 | 100 |

### ✅ **Classification Report**
```
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00       100
         1.0       1.00      1.00      1.00       100

    accuracy                           1.00       200
   macro avg       1.00      1.00      1.00       200
weighted avg       1.00      1.00      1.00       200
```

---
## 📌 Deployment Considerations
This model can be integrated into **real-world applications**, such as:
- **Mobile QR Code Scanners** → Detect counterfeit QR codes.
- **Payment Systems** → Prevent fraud by verifying QR codes.
- **Product Authentication** → Validate QR codes on packaging.

---
## 🎯 Future Improvements
✅ **Enhancing Dataset** → Adding more diverse QR codes.
✅ **Handling Noisy Scans** → Improving detection under bad lighting.
✅ **Deploying as an API** → Making it accessible via a web app.

---
## 🤝 Contributing
Want to improve this project? Follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-name`)
5. Open a Pull Request 🎉

