# 🧠 Employee Burnout Prediction and Recommendation System

## Overview

Employee burnout is one of the biggest challenges that organizations face today. High burnout levels can reduce productivity, increase absenteeism, and lead to employee turnover.

This project presents an intelligent system that predicts an employee's burnout level using Machine Learning based on workplace and personal factors. In addition to prediction, the system uses a Large Language Model (LLM) to explain the prediction and provide personalized recommendations that help reduce burnout and improve employee well-being.

The application is deployed using **Streamlit**, allowing HR professionals and managers to enter employee information, receive an instant burnout prediction, and obtain AI-generated recommendations in a simple and interactive interface.

---

## Problem Statement

Organizations often struggle to identify employees who are at risk of burnout before it starts affecting their performance. Traditional assessment methods are time-consuming and depend on manual evaluation.

This project aims to build an intelligent decision-support system that helps HR departments detect burnout early and provide recommendations that support employee well-being.

---

## Features

- Predict employee burnout rate using Machine Learning.
- Classify burnout risk into **Low**, **Medium**, or **High**.
- Explain the prediction using a Large Language Model (LLM).
- Generate practical recommendations based on employee information.
- Interactive web application built with Streamlit.

---

## Technologies Used

- Python
- Scikit-learn
- Pandas
- Streamlit
- Joblib
- Groq API 

---

## Machine Learning Model

The burnout prediction model was developed using a **XGBoost Regressor**, trained on employee workplace and psychological data.

### Input Features

- Gender
- Company Type
- WFH Setup Available
- Designation
- Resource Allocation
- Mental Fatigue Score
- Joining Date

### Output

- Burn Rate (0–1)
- Risk Level (Low, Medium, High)

---

## AI Recommendation

After predicting the burnout rate, the system sends the prediction and employee information to a Large Language Model (LLM), which provides:

- A brief explanation of the predicted burnout level.
- Three practical recommendations to help reduce burnout.

---

## Model Performance

| Metric | Score |
|--------|-------|
| R² Score | 0.9052 |
| MAE | 0.047 |
| MSE  | 0.0036 |
| RMSE | 0.061 |

---

## Deployment

The model is deployed as a Streamlit web application where users can:

1. Enter employee information.
2. Predict burnout rate.
3. View the burnout risk level.
4. Receive AI-powered recommendations instantly.
