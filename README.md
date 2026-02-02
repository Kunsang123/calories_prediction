Calories Burnt Prediction Project
Overview
This project leverages machine learning to predict the number of calories burnt during physical exercise. By analyzing factors such as age, gender, height, weight, exercise type, and duration, the system provides accurate estimates to support fitness and health monitoring.

The project encompasses:

Comprehensive data analysis and model training via Jupyter Notebook
A trained XGBoost model for prediction
A Django-based web application for user-friendly predictions
Datasets for exercise and calorie data
Features
Exploratory Data Analysis: In-depth data visualization and preprocessing
Machine Learning Pipeline: XGBoost-based regression model for calorie prediction
Web Interface: Intuitive Django application for real-time predictions
Data Sources: Curated datasets for model training and validation
Getting Started
Prerequisites
Python 3.8+
Git
Virtual environment (recommended)
Installation
Clone the Repository:
git clone https://github.com/Kunsang123/calories_prediction.git
cd calories_prediction

Set Up Environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Note: If requirements.txt is unavailable, install core dependencies: django, pandas, numpy, scikit-learn, xgboost, jupyter.

Run the Web Application:
cd calories_burnt_project
python manage.py migrate
python manage.py runserver

Navigate to http://127.0.0.1:8000/ in your browser.

Explore the Notebook:
jupyter notebook calories_prediction.ipynb

Usage
Data Analysis & Training: Execute calories_prediction.ipynb to perform EDA, train the model, and assess performance metrics.
Predictions: Use the web app to input parameters and receive calorie burn estimates.
Model Integration: Load calories_prediction_model.pkl for programmatic predictions.
Technologies
Programming Language: Python
Web Framework: Django
Data Science Tools: Jupyter Notebook, Pandas, NumPy
Machine Learning: Scikit-learn, XGBoost
Visualization: Matplotlib, Seaborn (as applicable)

Project Structure
calories_prediction/
├── calories_prediction.ipynb       # Analysis and model training notebook
├── calories.csv                    # Calorie dataset
├── exercise.csv                    # Exercise dataset
├── calories_prediction_model.pkl   # Serialized ML model
├── calories_burnt_project/         # Django web application
│   ├── manage.py
│   ├── config/                     # Django settings and configuration
    └── predictor/   

