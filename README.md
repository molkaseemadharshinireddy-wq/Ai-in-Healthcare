🩺 Pneumonia Detection using FastAI
📌 Overview

This project aims to detect Pneumonia from Chest X-ray images using Deep Learning techniques. It utilizes Transfer Learning with a pre-trained ResNet50 model implemented through the FastAI library.

The trained model is deployed using a Flask web application, enabling users to upload chest X-ray images and receive real-time predictions.

🎯 Objectives
Develop a robust deep learning model for medical image classification
Leverage transfer learning to improve accuracy and reduce training time
Classify chest X-ray images into:
Normal
Viral Pneumonia
Bacterial Pneumonia
Deploy the model as an interactive web application
🧠 Model Details
Architecture: ResNet50 (Pre-trained Convolutional Neural Network)
Framework: FastAI (built on PyTorch)
Technique: Transfer Learning & Fine-tuning
Task: Multi-class Image Classification
🗂️ Dataset
Source: Chest X-ray dataset (Kaggle)
Classes:
NORMAL
PNEUMONIA (Viral & Bacterial)
⚙️ Tech Stack
👨‍💻 Programming & Libraries
Python
FastAI
PyTorch
NumPy
Matplotlib
🌐 Deployment
Flask
🧪 Tools
Jupyter Notebook
🔄 Project Workflow
Data Collection
Dataset obtained from Kaggle
Data Preprocessing
Image resizing
Normalization
Dataset splitting (train/validation)
Model Training
Load pre-trained ResNet50
Apply transfer learning
Fine-tune the model using FastAI
Evaluation
Accuracy measurement
Confusion matrix analysis
Model Export
Save trained model as export.pkl
Deployment
Flask app loads trained model
User uploads X-ray image
Model predicts class and displays result
🚀 How to Run the Project
🔧 1. Clone the Repository
git clone https://github.com/Divyam6969/Pneumonia-Detection-using-FastAI.git
cd Pneumonia-Detection-using-FastAI
📦 2. Install Dependencies
pip install -r requirements.txt
▶️ 3. Run the Application
python app.py
🌐 4. Open in Browser
http://127.0.0.1:5000/
📊 Results
Achieved reliable classification performance using transfer learning
Model successfully distinguishes between normal and pneumonia cases
Confusion matrix used for evaluating prediction performance
🧪 Sample Output
Upload a chest X-ray image
Model predicts:
Normal
Viral Pneumonia
Bacterial Pneumonia
📸 Screenshots

(Add UI screenshots and prediction outputs here for better visualization)

⚠️ Limitations
Limited dataset size may affect generalization
No explainability techniques (e.g., Grad-CAM) implemented
Not validated for real-world clinical use
🔮 Future Improvements
Integrate explainable AI methods (Grad-CAM)
Train on larger and more diverse datasets
Improve accuracy using advanced architectures
Deploy on cloud platforms for scalability
🧾 Conclusion

This project demonstrates the effective use of Deep Learning and Transfer Learning in the healthcare domain for detecting pneumonia from chest X-ray images. By leveraging a pre-trained ResNet50 model with FastAI, the system achieves efficient and accurate image classification without requiring extensive computational resources.

The integration of the trained model into a Flask-based web application highlights the practical applicability of machine learning solutions in real-world scenarios. Despite certain limitations such as dataset size and lack of explainability, the project provides a strong foundation for further enhancements and deployment in medical diagnostics.

Overall, this project showcases an end-to-end pipeline — from data preprocessing and model training to deployment — making it a valuable contribution in the field of AI-driven healthcare solutions.
