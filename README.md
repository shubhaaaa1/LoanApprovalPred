# 💰 Loan Approval Prediction System

A machine learning-powered web application built with Streamlit that predicts whether a loan application will be approved based on user input. This project demonstrates data preprocessing, model training using ensemble learning, and deployment via Streamlit Cloud.

---

## 🚀 Features

* Interactive and user-friendly Streamlit UI
* Real-time loan status prediction
* Trained on real-world loan dataset
* Ensemble model: Voting Classifier (Logistic Regression, Decision Tree, Random Forest)
* Automatically handles missing values and categorical features

---

## 📊 Tech Stack

* **Frontend/UI**: Streamlit
* **Backend/ML**: Python, Scikit-learn, Pandas, NumPy
* **Deployment**: Streamlit Cloud

---

## 📁 Dataset

The model is trained on a cleaned version of a loan dataset, which includes features like:

* Gender
* Marital Status
* Education
* Self Employment
* Applicant & Co-applicant Income
* Loan Amount & Term
* Credit History
* Property Area

---

## 🧠 Model Details

An ensemble model is trained using the following classifiers:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

The predictions are combined using majority voting.

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/loan-approval-predictor.git
cd loan-approval-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push your code to a public GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and click **New App**.
3. Select your repo and `app.py` as the entry point.
4. Click **Deploy** — your app is live!

---

## 📷 Screenshot

![App Screenshot](screenshot.png) *(Replace with your own screenshot)*

---

## 👨‍💻 Author

**Shubham**
B.Tech CSE | ML Enthusiast | Streamlit Developer

Feel free to reach out or contribute!

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
