import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Churn Dashboard", layout="wide")

# ---------------- REMOVE TOP SPACE + DARK UI ----------------
st.markdown("""
<style>

/* Remove top padding completely */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 1rem !important;
}

/* Remove header space */
header {visibility: hidden;}

/* Dark background */
.stApp {
    background-color: #0e1117;
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    margin: 0;
    padding: 10px;
}

/* Inputs */
label, .stSelectbox, .stNumberInput {
    color: white !important;
}

/* Button */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 42px;
    width: 100%;
}

/* Remove extra spacing */
div[data-testid="stVerticalBlock"] {
    gap: 0.5rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">📊 Customer Churn Dashboard</div>', unsafe_allow_html=True)

# ---------------- TWO COLUMN FORM ----------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", [0, 1])
    dependents = st.selectbox("Dependents", [0, 1])
    tenure = st.slider("Tenure", 0, 72, 12)

    phone = st.selectbox("Phone Service", [0, 1])
    multiple = st.selectbox("Multiple Lines", [0, 1])
    internet = st.selectbox("Internet Service", [0, 1, 2])

with col2:
    security = st.selectbox("Online Security", [0, 1])
    backup = st.selectbox("Online Backup", [0, 1])
    device = st.selectbox("Device Protection", [0, 1])
    support = st.selectbox("Tech Support", [0, 1])

    tv = st.selectbox("Streaming TV", [0, 1])
    movies = st.selectbox("Streaming Movies", [0, 1])
    contract = st.selectbox("Contract", [0, 1, 2])

# ---------------- BILLING (INLINE) ----------------
col3, col4 = st.columns(2)

with col3:
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
    paperless = st.selectbox("Paperless Billing", [0, 1])

with col4:
    total = st.number_input("Total Charges", 0.0, 10000.0, 500.0)
    payment = st.selectbox("Payment Method", [0, 1, 2, 3])

# ---------------- BUTTON ----------------
predict_btn = st.button("🚀 Predict Churn")

# ---------------- PREDICTION ----------------
if predict_btn:

    data = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": device,
        "TechSupport": support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)

        if response.status_code == 200:
            result = response.json()

            if result["churn_prediction"] == 1:
                st.error("⚠️ Customer likely to churn")
            else:
                st.success("✅ Customer will stay")

            st.write(f"Probability: {result['churn_probability']:.2f}")
            st.write(f"Risk Level: {result['risk_level']}")

        else:
            st.error("API Error")

    except:
        st.error("⚠️ Backend not running. Start FastAPI first.")