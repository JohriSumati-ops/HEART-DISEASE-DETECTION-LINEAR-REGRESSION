import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

st.title("❤️ Heart Disease Prediction")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("heart.csv")

df = load_data()

# Prepare data
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train, y_train)

st.subheader("Enter Patient Details")

# Automatically create input fields
user_input = []
for col in X.columns:
    value = st.number_input(f"{col}", float(df[col].min()), float(df[col].max()))
    user_input.append(value)

if st.button("Predict"):
    user_array = np.array([user_input])
    user_scaled = scaler.transform(user_array)
    prediction = model.predict(user_scaled)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
