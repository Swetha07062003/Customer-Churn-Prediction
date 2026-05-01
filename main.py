import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# ==============================
# 1. LOAD DATA
# ==============================
print("🚀 Starting Churn Prediction Project")

df = pd.read_csv("data/telco_churn.csv")

# ==============================
# 2. DATA CLEANING
# ==============================

# Drop unnecessary column
df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

# Handle missing values (fixed warning properly)
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Convert target variable
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

print("\n✅ Data Cleaning Done")

# ==============================
# 3. ENCODING
# ==============================

le = LabelEncoder()

for col in df.select_dtypes(include=["object"]).columns:
    df[col] = le.fit_transform(df[col])

print("✅ Encoding Done")

# ==============================
# 4. SPLIT DATA
# ==============================

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("✅ Data Split Done")

# ==============================
# 5. TRAIN MODEL (IMBALANCE FIX)
# ==============================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("✅ Model Training Completed")

# ==============================
# 6. PREDICTION WITH THRESHOLD
# ==============================

y_prob = model.predict_proba(X_test)[:, 1]

# Adjust threshold (important for churn)
threshold = 0.3
y_pred = (y_prob > threshold).astype(int)

# ==============================
# 7. EVALUATION
# ==============================

print("\n📊 Model Evaluation")

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ==============================
# 8. CONFUSION MATRIX
# ==============================

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig("outputs/confusion_matrix.png")
plt.show()

print("✅ Confusion Matrix Saved in outputs/")

# ==============================
# 9. FEATURE IMPORTANCE
# ==============================

importance = model.feature_importances_
features = X.columns

feat_imp = pd.Series(importance, index=features).sort_values(ascending=False)

print("\n🔥 Top 10 Important Features:\n")
print(feat_imp.head(10))

# Save feature importance
feat_imp.to_csv("outputs/feature_importance.csv")

print("\n✅ Feature Importance Saved")

print("\n🎯 Project Completed Successfully")
import joblib

joblib.dump(model, "models/churn_model.pkl")

print("\n✅ Model Saved Successfully (models/churn_model.pkl)")