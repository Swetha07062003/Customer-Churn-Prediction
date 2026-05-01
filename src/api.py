from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load model
model = joblib.load("models/model.pkl")

app = FastAPI(title="Customer Churn Prediction API")

# -----------------------------
# INPUT SCHEMA
# -----------------------------
class Customer(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float

# -----------------------------
# HOME
# -----------------------------
@app.get("/")
def home():
    return {"message": "Churn API Running 🚀"}

# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/health")
def health():
    return {"status": "OK"}

# -----------------------------
# SINGLE PREDICTION
# -----------------------------
@app.post("/predict")
def predict(data: Customer):
    input_data = np.array([list(data.dict().values())])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(probability), 2),
        "risk_level": "High" if probability > 0.6 else "Low"
    }

# -----------------------------
# BATCH PREDICTION (FIXED ERROR)
# -----------------------------
@app.post("/batch_predict")
def batch_predict(data: list[Customer]):
    inputs = np.array([list(d.dict().values()) for d in data])
    
    preds = model.predict(inputs)
    probs = model.predict_proba(inputs)[:, 1]

    results = []
    for p, pr in zip(preds, probs):
        results.append({
            "prediction": int(p),
            "probability": round(float(pr), 2)
        })

    return {"results": results}

# -----------------------------
# EXPLAIN ENDPOINT
# -----------------------------
@app.post("/predict")
def predict(customer: Customer):

    x = [customer.dict()]

    # Probability
    prob = float(model.predict_proba(x)[0][1])

    # Prediction
    pred = int(prob >= 0.5)

    # ✅ FIXED RISK LOGIC
    if prob >= 0.65:
        risk = "High"
    elif prob >= 0.35:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "churn_prediction": pred,
        "churn_probability": prob,
        "risk_level": risk
    }