🩺 AI in Healthcare: Pneumonia Detection System
📌 Overview

This project focuses on applying Artificial Intelligence in Healthcare to detect Pneumonia from Chest X-ray images. It uses Deep Learning and Computer Vision techniques to automatically classify medical images into different categories.

A pre-trained Convolutional Neural Network (ResNet50) is used with Transfer Learning, enabling efficient and accurate predictions. The model is integrated into a Flask-based web application, allowing users to upload X-ray images and receive real-time diagnostic predictions.

🎯 Objectives
Develop an AI-based system for pneumonia detection
Apply transfer learning to improve performance
Classify chest X-ray images into:
Normal
Viral Pneumonia
Bacterial Pneumonia
Build a user-friendly web interface for predictions
🧠 Model Details
Architecture: ResNet50 (Pre-trained CNN)
Framework: FastAI (built on PyTorch)
Technique: Transfer Learning & Fine-tuning
Task: Multi-class Image Classification
🗂️ Dataset
Chest X-ray image dataset
Categories:
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
Gather chest X-ray images
Data Preprocessing
Image resizing
Normalization
Train-validation split
Model Training
Load pre-trained ResNet50
Apply transfer learning
Fine-tune model
Evaluation
Measure accuracy
Analyze confusion matrix
Model Export
Save trained model as export.pkl
Deployment
Flask app loads trained model
User uploads X-ray image
Model predicts result
🚀 How to Run the Project
🔧 1. Clone the Repository
git clone https://github.com/molkaseemadharshinireddy-wq/Ai-in-Healthcare.git
cd Ai-in-Healthcare
📦 2. Install Dependencies
pip install -r requirements.txt
▶️ 3. Run the Application
python app.py
🌐 4. Open in Browser
http://127.0.0.1:5000/
📊 Results
Achieved effective classification using transfer learning
Model distinguishes between normal and pneumonia cases
Provides quick predictions through a web interface
🧪 Sample Output
Upload an X-ray image
Model predicts:
Normal
Viral Pneumonia
Bacterial Pneumonia
🧾 Conclusion

This project demonstrates the potential of Artificial Intelligence in healthcare by developing an automated system for pneumonia detection using chest X-ray images. By leveraging transfer learning with a ResNet50 model, the system achieves efficient and reliable performance without extensive computational requirements.

The integration of the trained model into a Flask web application showcases its real-world usability, enabling users to interact with the system easily. Although improvements can be made in terms of dataset size and explainability, the project successfully presents an end-to-end AI solution — from data preprocessing and model training to deployment.

Overall, this project highlights how deep learning can assist in early detection and diagnosis, contributing to advancements in medical technology.
