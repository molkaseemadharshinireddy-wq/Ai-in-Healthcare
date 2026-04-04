from flask import Flask, render_template, request
from fastai.vision.learner import load_learner
from fastai.vision.core import PILImage
from werkzeug.utils import secure_filename
from pathlib import Path
app = Flask(__name__)

# Load model
learn_inf = load_learner(r"C:\project\export.pkl")

class_labels = {
    'VIRAL': {
        'label': 'Viral Pneumonia',
        'description': 'Viral pneumonia is an infection of the lungs caused by a virus.',
        'risk_factors': 'Flu, RSV, weak immunity'
    },
    'BACTERIAL': {
        'label': 'Bacterial Pneumonia',
        'description': 'Bacterial pneumonia is caused by bacteria.',
        'risk_factors': 'Streptococcus, smoking, lung disease'
    },
    'NORMAL': {
        'label': 'Normal',
        'description': 'No pneumonia detected.',
        'risk_factors': 'Healthy lungs'
    }
}

def predict_img(img_path):
    img = PILImage.create(img_path)
    pred, _, _ = learn_inf.predict(img)
    return str(pred)   # 🔥 VERY IMPORTANT

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def get_output():
    img = request.files['my_image']
    img_path = "static/" + secure_filename(img.filename)

    Path("static").mkdir(exist_ok=True)
    img.save(img_path)

    prediction = predict_img(img_path)

    result = class_labels.get(prediction, {
        'label': 'Unknown',
        'description': '',
        'risk_factors': ''
    })

    return render_template("index.html",
                           prediction=result['label'],
                           description=result['description'],
                           risk_factors=result['risk_factors'],
                           img_path=img_path)

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)