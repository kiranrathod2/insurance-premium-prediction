# 🚀 Insurance Premium Prediction Web App

This repository contains a **Flask-based web application** that predicts **insurance premiums** using a **Decision Tree Machine Learning model**.  
Users can fill out a web form with details such as **age, gender, region, marital status, dependants, BMI category, smoking habits, employment, income, medical history, and insurance plan**.  
The app processes these inputs, scales them, and predicts the premium amount.

---

**📌Project Overview**

The goal of this project is to build a predictive model that estimates the insurance premium a person has to pay based on several features such as:

 Age

 Gender

 BMI (Body Mass Index)

 Smoking Status

 Number of Dependents

 Region

 Marital Status

 Income

By analyzing these features, the model learns hidden patterns and provides an estimated premium value.

**⚙️ Tech Stack**

Python

Pandas, NumPy – Data manipulation & preprocessing

Matplotlib, Seaborn – Data visualization

Scikit-learn – Model building & evaluation

Flask – Web application for deployment

**🚀 Workflow**

Data Collection & Cleaning – Process raw dataset, handle missing values, and encode categorical variables.

Exploratory Data Analysis (EDA) – Understand relationships between features and premium.

Feature Engineering – Transform inputs for better model performance.

Model Training – Train regression models (e.g., Linear Regression, Decision Tree, Random Forest, etc.).

Model Evaluation – Compare models using metrics like MAE, RMSE, and R².

Deployment – Deploy best model using Flask for real-time premium prediction.

**🌐 Web App Features**

User-friendly form to input customer details.

Predicts insurance premium instantly.

Displays prediction results clearly.

**📊 Example Use Case**

👉 A 35-year-old male, smoker, with BMI 28 and 2 dependents can get a quick estimate of the premium he might have to pay.

**📂 Project Structure**

├── static/              # CSS, JS, images
├── templates/           
│   └── index.html       # Main HTML page (Flask template)
├── model.pkl            # Trained ML model
├── app.py               # Flask application
├── requirements.txt     # Required libraries
└── README.md            # Project documentation

**🛠️ Installation & Usage**

1️⃣ Clone the Repository
git clone https://github.com/kiranrathod2/insurance-premium-prediction.git
cd insurance-premium-prediction

2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
python app.py

5️⃣ Open in Browser

👉 http://127.0.0.1:5000/

Enter user details in the form and get an instant insurance premium prediction.

**🔮 Future Improvements**

Add more advanced models (XGBoost, CatBoost).

Build an interactive dashboard with Streamlit.

Integrate with SQL/NoSQL databases for scalability.

Add API support for mobile applications.

**📌 Conclusion**

This project demonstrates how Machine Learning can be applied in the insurance industry to predict health premiums efficiently, supporting data-driven decision-making and enhancing customer experience.

**📬 Contact**

GitHub: [kiranrathod2](https://github.com/kiranrathod2)

Email: kiranrathod2602@gmail.com

LinkedIn: www.linkedin.com/in/kiran-rathod-605919367


