from pathlib import Path

from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from joblib import load

app = Flask(__name__)

# Resolve artifacts relative to this file so the app works from any CWD.
BASE_DIR = Path(__file__).resolve().parent
model = tf.keras.models.load_model(BASE_DIR / 'diabetes_model.h5')
scaler = load(BASE_DIR / 'scaler.joblib')

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_page_or_api():
    if request.method == 'GET':
        return render_template('index.html')

    # Backward-compatible POST handler for clients still calling /predict.
    return run_prediction()

@app.route('/api/predict', methods=['POST'])
def predict():
    return run_prediction()


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


def run_prediction():
    try:
        # Get the data from the request
        data = request.get_json(silent=True) or {}
        
        # Extract features in the correct order
        # Support both diabetes_pedigree and legacy diabetesPedigreeFunction keys.
        features = [
            float(data['pregnancies']),
            float(data['glucose']),
            float(data['blood_pressure']),
            float(data['skin_thickness']),
            float(data['insulin']),
            float(data['bmi']),
            float(data.get('diabetes_pedigree', data.get('diabetesPedigreeFunction', 0.0))),
            float(data['age'])
        ]
        
        # Convert to numpy array and reshape
        features = np.array(features).reshape(1, -1)
        
        # Scale the features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled, verbose=0)
        probability = float(prediction[0][0])
        
        # Determine the result and confidence
        result = 'Diabetic' if probability >= 0.5 else 'Not Diabetic'
        confidence = probability if result == 'Diabetic' else (1 - probability)
        
        # Return the prediction result
        return jsonify({
            'result': result,
            'probability': probability,
            'confidence': confidence,
            'probability_pct': round(probability * 100, 2),
            'confidence_pct': round(confidence * 100, 2)
        })
        
    except KeyError as e:
        return jsonify({
            'error': f'Missing required field: {str(e)}'
        }), 400
    except ValueError:
        return jsonify({
            'error': 'Invalid numeric value in request payload'
        }), 400
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return jsonify({
            'error': 'An error occurred while making the prediction',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)