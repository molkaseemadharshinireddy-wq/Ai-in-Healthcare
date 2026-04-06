# Chest X-ray Pneumonia Detection
This project detects pneumonia from chest X-ray images using a deep learning approach. A pretrained ResNet50 model is used with transfer learning through the fastAI library. The model is integrated into a Flask web application where users can upload an image and view the prediction.

## Objectives
- Develop a deep learning model for image classification  
- Use transfer learning to improve performance  
- Classify chest X-ray images into:
  - Normal  
  - Viral Pneumonia  
  - Bacterial Pneumonia  
- Deploy the model using a web application  

## Model Details
- Architecture: ResNet50  
- Framework: fastAI (PyTorch-based)  
- Technique: Transfer Learning  
- Task: Image Classification  

## Dataset
- Source: Chest X-ray dataset (Kaggle)  
- Classes:
  - Normal  
  - Pneumonia (Viral & Bacterial)  

## Tech Stack
- Python  
- fastAI  
- PyTorch  
- NumPy  
- Flask  
- HTML / CSS  

## Workflow
- Data Collection  
- Data Preprocessing (resizing, normalization)  
- Model Training & Testing  
- Model Export (`export.pkl`)  
- Deployment using Flask  
- Image Upload → Prediction → Result Display  

## How to Run
1. Install dependencies  
2. Run:
   python app.py  

## Results
- Model classifies X-ray images into normal and pneumonia  
- Works well on most test cases  
- Predictions are displayed through the web interface  

## Conclusion
This project demonstrates the use of deep learning for detecting pneumonia from chest X-ray images. The system is simple, efficient, and provides quick predictions through a web application. It serves as a basic example of applying AI in healthcare.
