import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")

model = joblib.load("model.pkl")

st.title("Churn Prediction Application")

st.divider()

st.write("Please enter the values and hit the Submit button for getting the Prediction.")

st.divider()

age = st.number_input("Enter Age between 10 - 100", min_value = 10, max_value = 100, value = 30)

tenure = st.number_input("Enter Tenure between 0 - 130", min_value = 0, max_value = 130, value = 10)

monthlycharge = st.number_input("Enter Monthly Charge between 30 - 150", min_value = 30, max_value = 150)

gender = st.selectbox("Select Gender", ["Male", "Female"])

st.divider()

predict_button = st.button("Submit")

st.divider()

if predict_button:
    
    gender_selected = 1 if gender == "Female" else 0
    
    X = [age, gender_selected, tenure, monthlycharge]
    
    X1 = np.array(X)
    
    X_array = scaler.transform([X1])
    
    prediction = model.predict(X_array)[0]
    
    predicted = "Yes" if prediction == 1 else "No"
    
    st.balloons()
    
    st.write(f"Churn Prediction: {predicted}")
    
else:
    
    st.write("Please enter the values and press 'Submit Button'")

st.divider()

st.header("Created by SAI LINGESH R")

st.caption("www.linkedin.com/in/sai-lingesh")