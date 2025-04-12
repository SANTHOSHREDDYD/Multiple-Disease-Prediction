# Disease Prediction Project

This project is a complete Machine Learning and Web Application system for predicting multiple diseases — including Diabetes, Cancer, Heart Disease, and Parkinson's — using a clean frontend and backend pipeline.

---

## 🏥 Project Overview
- **Frontend**: HTML, CSS, JavaScript based form for input and prediction display.
- **Backend**: Machine Learning models trained using SVM, Logistic Regression, and Random Forest.
- Predicts: Diabetes, Cancer, Heart Disease, Parkinson's.

---

## 💻 Files Overview

| File Name                        | Purpose                                           |
|----------------------------------|---------------------------------------------------|
| `index.html`                     | Main frontend form for user input.                |
| `index.css`                      | Styling for the frontend UI.                      |
| `script.js`                      | Handles input validation and mock prediction logic. |
| `Disease_Prediction_Model.py`    | Machine learning model code for all diseases.     |
| `README.md`                      | Project documentation.                           |

---

## 🚀 How to Run

### Backend (Machine Learning)
1. Install dependencies:
```bash
pip install pandas numpy scikit-learn
```
2. Make sure your data files (`diabetes.csv`, `cancer.csv`, `heart.csv`, `parkinsons.csv`) are in the same directory.
3. Run the model script:
```bash
python Disease_Prediction_Model.py
```

---

### Frontend (Web App)
1. Place `index.html`, `index.css`, and `script.js` in the same directory.
2. Open `index.html` using any web browser.
3. Enter your age, gender, and symptoms, and click **Predict Disease**.

---

## ⚡ Features
- Predict multiple diseases based on different datasets.
- Easy-to-use form interface.
- Supports multiple algorithms: SVM, Logistic Regression, Random Forest.
- Clean, responsive and professional UI design.

---

## ⚙️ Customization
- Replace the `predictDisease()` logic in `script.js` with a real API endpoint once your model is deployed.
- Update the background image URL or add animations in `index.css` for better design customization.

---

## 💡 Future Improvements
- Connect the frontend to a live backend using Flask or FastAPI.
- Deploy models using cloud services like AWS, Heroku, or Streamlit.
- Add real-time chart visualizations for prediction confidence.

---

## 📜 License
This project is open-source and free to use for educational and personal projects.

---

If you'd like, I can help you set up a Flask server for live prediction too!

