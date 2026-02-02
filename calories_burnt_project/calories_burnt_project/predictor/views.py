from django.shortcuts import render
import os
import pickle
from django.conf import settings


def index(request):
	prediction = None
	error = None
	if request.method == 'POST':
		try:
			# Expected features from model: Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp
			gender_raw = request.POST.get('gender', '')
			# map possible inputs to model encoding: male->0, female->1
			if gender_raw.lower() in ('male', 'm', '0'):
				gender = 0
			elif gender_raw.lower() in ('female', 'f', '1'):
				gender = 1
			else:
				# try numeric
				try:
					gender = int(gender_raw)
				except Exception:
					gender = 0

			age = float(request.POST.get('age', 30))
			height = float(request.POST.get('height', 170))
			weight = float(request.POST.get('weight', 70))
			duration = float(request.POST.get('duration', 30))
			heart_rate = float(request.POST.get('heart_rate', 100))
			body_temp = float(request.POST.get('body_temp', 37))

			# fallback placeholder (MET-based) using default MET=6
			prediction = round(0.0175 * 6 * weight * duration, 2)

			# Try to load configured model at config/calories_prediction_model.pkl
			model_path = os.path.join(settings.BASE_DIR, 'config', 'calories_prediction_model.pkl')
			if os.path.exists(model_path):
				try:
					with open(model_path, 'rb') as f:
						model = pickle.load(f)
					# Prepare features in the order expected by the model
					features = [[gender, age, height, weight, duration, heart_rate, body_temp]]
					pred = model.predict(features)
					prediction = float(pred[0])
				except Exception:
					# keep placeholder if model call fails
					pass

		except Exception:
			error = 'Invalid input. Please enter numeric values for the fields.'

	return render(request, 'predictor/index.html', {'prediction': prediction, 'error': error})
