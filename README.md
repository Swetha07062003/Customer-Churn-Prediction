# 📊 Customer Churn Prediction

This project predicts whether a customer is likely to churn using Machine Learning.  
It includes data preprocessing, model training, FastAPI backend, and a Streamlit dashboard.

---

## 🚀 Features

- 🔍 Data preprocessing and feature engineering
- 🤖 Machine Learning model (Churn Prediction)
- ⚡ FastAPI backend for predictions
- 🎯 Streamlit interactive dashboard
- 📊 Feature importance and confusion matrix visualization

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── data/
│   └── telco_churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── outputs/
│   ├── confusion_matrix.png
│   └── feature_importance.csv
│
├── images/
│   ├── api.png
│   ├── dashboard.png
│   ├── positive.png
│   └── negative.png
│
├── src/
│   ├── api.py
│   ├── preprocess.py
│   └── train.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:
```
git clone https://github.com/Swetha07062003/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

2. Install dependencies:
```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 1️⃣ Train Model
```
python src/train.py
```

### 2️⃣ Run FastAPI Server
```
uvicorn src.api:app --reload
```

👉 API runs at: http://127.0.0.1:8000/docs

---

### 3️⃣ Run Dashboard
```
streamlit run app.py
```

👉 Dashboard runs at: http://localhost:8501

---

## 📊 Model Details

- Dataset: Telco Customer Churn Dataset
- Algorithm: Classification Model (e.g., Logistic Regression / Random Forest)
- Output:
  - Churn Prediction (0 / 1)
  - Probability Score
  - Risk Level (Low / Medium / High)

Customer churn prediction helps businesses reduce customer loss and improve retention strategies. :contentReference[oaicite:1]{index=1}

---

## 🖥️ Screenshots

### 📌 API
![API](images/api.png)

### 📌 Dashboard
![Dashboard](images/dashboard.png)

### 📌 Churn Prediction (Positive)
![Positive](images/positive.png)

### 📌 Churn Prediction (Negative)
![Negative](images/negative.png)

---

## 📌 Future Improvements

- 🔍 Add SHAP for explainability
- ☁️ Deploy on cloud (AWS / Render / Railway)
- 🔄 Add real-time prediction support

---

## 👩‍💻 Author

Swetha K  
 
---

