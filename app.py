from flask import Flask, render_template, request
import pickle as pk
import pandas as pd

app = Flask(__name__)

model = pk.load(open("dt_model.pkl", "rb"))
scaler = pk.load(open("scaler.pkl", "rb"))
encoders = pk.load(open("encoders.pkl", "rb"))

def get_dropdown_data():
    return dict(gender=encoders["Gender"].classes_,
        region=encoders["Region"].classes_,
        smoking=encoders["Smoking_Status"].classes_,
        Marital_status=encoders["Marital_status"].classes_,
        bmi=encoders["BMI_Category"].classes_,
        employment=encoders["Employment_Status"].classes_,
        medical=encoders["Medical History"].classes_,
        insurance=encoders["Insurance_Plan"].classes_)

@app.route("/")
def home():
    return render_template("index.html", **get_dropdown_data())

@app.route("/predict", methods=["POST"])
def predict_insurance_premium():

    age = int(request.form["Age"])
    gender = encoders["Gender"].transform([request.form["Gender"]])[0]
    region = encoders["Region"].transform([request.form["Region"]])[0]
    Marital_status = encoders["Marital_status"].transform([request.form["Marital_status"]])[0]
    dependants = int(request.form["Number Of Dependants"])
    bmi = encoders["BMI_Category"].transform([request.form["BMI_Category"]])[0]
    smoking = encoders["Smoking_Status"].transform([request.form["Smoking_Status"]])[0]
    employment = encoders["Employment_Status"].transform([request.form["Employment_Status"]])[0]
    income = float(request.form["Income_Level"])
    income_lakhs = float(request.form["Income_Lakhs"])
    medical = encoders["Medical History"].transform([request.form["Medical History"]])[0]
    insurance = encoders["Insurance_Plan"].transform([request.form["Insurance_Plan"]])[0]

    pred_data = pd.DataFrame([[age, gender, region, Marital_status, dependants, bmi, smoking,
          employment, income, income_lakhs, medical, insurance]],
          columns=["Age", "Gender", "Region", "Marital_status", "Number Of Dependants",
                    "BMI_Category", "Smoking_Status", "Employment_Status",
                    "Income_Level", "Income_Lakhs", "Medical History", "Insurance_Plan"])

    scaled_data = scaler.transform(pred_data)
    prediction = int(model.predict(scaled_data)[0])

    return render_template("index.html",prediction_text=f"Predicted Premium: {prediction}/-",**get_dropdown_data())

if __name__ == "__main__":
    app.run(debug=True)






