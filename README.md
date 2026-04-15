<div align="center">

# DiabetesCare: Diabetes Risk Assessment System

An end-to-end ML-powered web application for diabetes risk prediction with a modern interface, production-ready API, and free-cloud deployment.

[![Live App](https://img.shields.io/badge/Live-HuggingFace%20Space-blue?logo=huggingface&logoColor=white)](https://manikantaperla-diabatescare.hf.space)
[![Space](https://img.shields.io/badge/Hugging%20Face-Space-yellow?logo=huggingface&logoColor=black)](https://huggingface.co/spaces/Manikantaperla/diabatescare)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

[![GitHub stars](https://img.shields.io/github/stars/ManikantaPerla07/DiabatesCare?style=social)](https://github.com/ManikantaPerla07/DiabatesCare/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ManikantaPerla07/DiabatesCare?style=social)](https://github.com/ManikantaPerla07/DiabatesCare/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/ManikantaPerla07/DiabatesCare)](https://github.com/ManikantaPerla07/DiabatesCare/commits/master)
[![Open Issues](https://img.shields.io/github/issues/ManikantaPerla07/DiabatesCare)](https://github.com/ManikantaPerla07/DiabatesCare/issues)

</div>

## Table of Contents

- [Live Demo](#live-demo)
- [Screenshots](#screenshots)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [API Reference](#api-reference)
- [Local Setup](#local-setup)
- [Docker Run](#docker-run)
- [Roadmap](#roadmap)
- [Project Structure](#project-structure)
- [Notes](#notes)
- [Contributing](#contributing)
- [Acknowledgment](#acknowledgment)

## Live Demo

- App URL: https://manikantaperla-diabatescare.hf.space
- Space URL: https://huggingface.co/spaces/Manikantaperla/diabatescare
- GitHub Repo: https://github.com/ManikantaPerla07/DiabatesCare

## Screenshots

Project screenshots can be added under `docs/screenshots/`.

- Landing Page: `docs/screenshots/landing-page.png`
- Prediction Form: `docs/screenshots/prediction-form.png`
- Result View: `docs/screenshots/prediction-result.png`

## Key Features

- Clean and responsive UI for health data input
- Real-time diabetes risk prediction using TensorFlow
- Clear result summary with risk and safety percentages
- Visual chart breakdown of prediction probabilities
- Actionable recommendation panel based on result
- Flask API endpoint for programmatic prediction
- Dockerized deployment for portable hosting

## Tech Stack

- Backend: Flask
- ML Inference: TensorFlow (CPU), NumPy, scikit-learn, Joblib
- Frontend: HTML, CSS, JavaScript, Bootstrap, Chart.js
- Deployment: Docker on Hugging Face Spaces

## How It Works

1. User enters clinical inputs on the prediction form.
2. Backend validates and normalizes inputs.
3. Stored StandardScaler transforms feature values.
4. TensorFlow model predicts diabetes probability.
5. API returns result, probability, confidence, and percentages.
6. Frontend renders a readable summary, chart, and recommendations.

## API Reference

### Health Check

- Method: `GET`
- Endpoint: `/health`
- Response:

```json
{
	"status": "ok"
}
```

### Predict Risk

- Method: `POST`
- Endpoint: `/api/predict`
- Content-Type: `application/json`

Request body example:

```json
{
	"pregnancies": 2,
	"glucose": 135,
	"blood_pressure": 80,
	"skin_thickness": 25,
	"insulin": 85,
	"bmi": 29.7,
	"diabetes_pedigree": 0.52,
	"age": 41
}
```

Response example:

```json
{
	"result": "Diabetic",
	"probability": 0.74,
	"confidence": 0.74,
	"probability_pct": 74.0,
	"confidence_pct": 74.0
}
```

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/ManikantaPerla07/DiabatesCare.git
cd DiabatesCare
```

### 2. Create and Activate Virtual Environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Open: `http://127.0.0.1:5000`

## Docker Run

```bash
docker build -t diabetescare .
docker run -p 7860:7860 diabetescare
```

Then open: `http://localhost:7860`

## Roadmap

- Add model versioning and model metadata endpoint
- Add input range hints and inline validation messages in the UI
- Add downloadable PDF summary of predictions
- Add lightweight test suite for API and frontend interactions
- Add CI workflow for linting and deployment checks
- Improve accessibility for charts and color-blind-safe palettes

## Project Structure

```text
DiabatesCare/
	app.py                   # Flask routes and prediction API
	diabetes_model.h5        # Trained TensorFlow model
	scaler.joblib            # StandardScaler for feature normalization
	requirements.txt         # Python dependencies
	Dockerfile               # Container build for deployment
	templates/
		landing.html           # Landing page
		index.html             # Prediction form and result view
	static/
		css/style.css          # Styles
		js/main.js             # Client-side interactions
```

## Notes

- This project is for educational and screening support purposes only.
- Predictions are not a medical diagnosis.
- Always consult a qualified healthcare professional for clinical decisions.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make focused changes with clear commit messages.
4. Open a pull request describing the change and expected impact.

For detailed contribution guidelines, see `CONTRIBUTING.md`.

## Acknowledgment

Built and maintained by Manikanta Perla.
