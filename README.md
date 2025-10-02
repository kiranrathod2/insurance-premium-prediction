# insurance-premium-prediction
Flask web app for predicting insurance premiums using Machine Learning

# 🚀 Insurance Premium Prediction Web App

This repository contains a **Flask-based web application** that predicts **insurance premiums** using a **Decision Tree Machine Learning model**.  
Users can fill out a web form with details such as **age, gender, region, marital status, dependants, BMI category, smoking habits, employment, income, medical history, and insurance plan**.  
The app processes these inputs, scales them, and predicts the premium amount.

---

## 📌 Features
- 🧠 ML model (Decision Tree) trained with real-world insurance dataset  
- 🌐 Flask backend with HTML templates  
- 📝 User-friendly dropdowns and form inputs  
- 🔄 Automatic label encoding for categorical values  
- 📊 Premium prediction in real-time  

---

## 🛠 Tech Stack
- **Backend:** Python, Flask  
- **ML Libraries:** Scikit-learn, Pandas, NumPy  
- **Frontend:** HTML, CSS (via `templates/index.html`)  
- **Deployment:** Flask server  

---

📂 Project Structure
├── app.py                  # Flask application
├── dt_model.pkl            # Saved Decision Tree model
├── scaler.pkl              # Scaler for preprocessing
├── encoders.pkl            # Label encoders for categorical features
├── templates/
│   └── index.html          # Frontend form
├── static/                 # (Optional) CSS/JS files
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

