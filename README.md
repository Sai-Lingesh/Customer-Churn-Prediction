# Customer Churn Prediction

This repository contains a **Customer Churn Prediction Application** built using **Streamlit** and a Jupyter Notebook for the data analysis and model training process. The app predicts whether a customer is likely to churn based on input features such as age, gender, tenure, and monthly charges.

## Features

- **Streamlit Web Application**: An interactive interface for users to input customer details and predict churn probability.
- **Customer Churn Prediction Model**: A machine learning model trained to classify customer churn using historical data.

---

## Repository Structure

```
├── app.py                          # Streamlit web app for churn prediction
├── Customer Churn Prediction.ipynb # Jupyter Notebook for data analysis and model training
├── scaler.pkl                      # Scaler used for data preprocessing (loaded in app.py)
├── model.pkl                       # Trained machine learning model (loaded in app.py)
```

---

## Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/churn-prediction.git
   cd churn-prediction
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   > Note: Ensure you have Python 3.7+ installed.

3. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Access the app in your browser at `http://localhost:8501`.

---

## Files Overview

### 1. `app.py`

This is the main file for the **Streamlit Churn Prediction Application**. It:

- Loads the **trained model** (`model.pkl`) and **scaler** (`scaler.pkl`).
- Accepts user input (age, gender, tenure, and monthly charges).
- Predicts customer churn and displays the result interactively.

### 2. `Customer Churn Prediction.ipynb`

This Jupyter Notebook includes:

- **Exploratory Data Analysis (EDA)**: Insights into the dataset used for training.
- **Feature Engineering**: Preparation of data for machine learning.
- **Model Training and Evaluation**: Development and testing of the churn prediction model.

---

## Inputs for Prediction

The following inputs are required for making predictions:

- **Age**: Customer's age (10 - 100 years).
- **Tenure**: Number of months the customer has been with the company (0 - 130 months).
- **Monthly Charge**: Monthly amount paid by the customer (30 - 150 currency units).
- **Gender**: Male or Female.

---

## Results

The model predicts whether a customer is likely to churn with a "Yes" or "No" response. The app uses a pre-trained machine learning model for this classification.

---

## Author

Created by **Sai Lingesh R**  
[LinkedIn Profile](https://www.linkedin.com/in/sai-lingesh)
