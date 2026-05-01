import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.preprocess import preprocess_data

# Load dataset
df = pd.read_csv("data/telco_churn.csv")

# Preprocess
df = preprocess_data(df)

# Split
X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/model.pkl")

print("✅ Model trained & saved!")