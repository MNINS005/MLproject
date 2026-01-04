📊 Student Performance Prediction – ML Web App

A Machine Learning–based web application that predicts student math scores based on demographic and academic features.
The project uses a scikit-learn pipeline, trained ML models, and a Flask web interface for real-time predictions.

🚀 Project Overview

This project demonstrates an end-to-end Machine Learning workflow, including:

->Data ingestion and preprocessing

->Feature engineering using ColumnTransformer

->Model training and hyperparameter tuning

->Saving trained artifacts (model & preprocessor)

->Serving predictions through a Flask web application

->The application takes user input from a web form and returns a predicted math score.

🧠 Machine Learning Pipeline
Key ML Concepts Used

->Data preprocessing with Pipeline & ColumnTransformer

->Handling categorical and numerical features

->Model comparison and hyperparameter tuning

->Artifact-based inference (no retraining during prediction)

->Models Used

->Linear Regression

->Decision Tree Regressor

->Random Forest Regressor

->Gradient Boosting Regressor

->XGBoost Regressor

->CatBoost Regressor

->AdaBoost Regressor

The best-performing model is selected based on evaluation metrics.

🏗️ Project Structure
ML project/
│
├── app.py                  # Flask application entry point
├── templates/              # HTML templates
│   ├── index.html
│   └── home.html
│
├── src/
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── utils.py
│   ├── logger.py
│   └── exceptions.py
│
├── artifacts/              # Saved models & preprocessors (ignored in Git)
├── requirements.txt
└── README.md

🌐 Web Application Flow
User Input (Browser)
        ↓
Flask Backend
        ↓
Load preprocessor.pkl
        ↓
Transform input data
        ↓
Load model.pkl
        ↓
Prediction
        ↓
Result displayed on web page



⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <https://github.com/MNINS005/Score_predictor.git>
cd ML-project

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application
python app.py


Open your browser and go to:

http://127.0.0.1:5000/
