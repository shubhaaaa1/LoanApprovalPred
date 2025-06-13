import streamlit as st
import numpy as np
import pickle

# Page Configuration
st.set_page_config(page_title="Loan Approval Predictor", page_icon="💰", layout="centered")
st.title("💰 Loan Approval Prediction System")
st.markdown("""
Welcome to the intelligent Loan Approval Predictor. 
Fill out the details below and find out if your loan application might be approved.
""")

# Input UI
col1, col2 = st.columns(2)

with col1:
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    ApplicantIncome = st.number_input("Applicant Income(in thousands)", min_value=0)
    CoapplicantIncome = st.number_input("Coapplicant Income (in thousands)", min_value=0)
    LoanAmount = st.number_input("Loan Amount (in thousands)", min_value=0)
    Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", min_value=0)
    Credit_History = st.selectbox("Credit History", ["Has Credit History", "No Credit History"])
    Property_Area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Encoding maps
gender_map = {"Male": 1, "Female": 0}
married_map = {"Yes": 1, "No": 0}
education_map = {"Graduate": 1, "Not Graduate": 0}
self_employed_map = {"Yes": 1, "No": 0}
credit_map = {"Has Credit History": 1, "No Credit History": 0}
property_map = {"Rural": 0, "Semiurban": 1, "Urban": 2}
dependents_map = {"0": 0, "1": 1, "2": 2, "3+": 3}

# Load trained model
@st.cache_resource
def load_model():
    with open("loan_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Prediction logic
if st.button("🔍 Predict Loan Status"):
    features = [
        gender_map[Gender],
        married_map[Married],
        dependents_map[Dependents],
        education_map[Education],
        self_employed_map[Self_Employed],
        ApplicantIncome,
        CoapplicantIncome,
        LoanAmount,
        Loan_Amount_Term,
        credit_map[Credit_History],
        property_map[Property_Area]
    ]

    prediction = model.predict([features])
    result = "✅ Approved" if prediction[0] == 1 else "❌ Rejected"
    st.success(f"Loan Prediction Result: {result}")
    st.balloons()

