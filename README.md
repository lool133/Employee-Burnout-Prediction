# Employee Burnout Prediction

## Overview
Employee burnout is a major challenge that affects productivity, employee satisfaction, and organizational performance. This project applies Machine Learning techniques to predict employee burnout levels using workplace and employee-related data, enabling organizations to identify at-risk employees early and take proactive actions.

---

## Problem Statement
Many companies lose valuable employees due to psychological burnout, but the warning signs are often recognized only after it is too late.

This project aims to build a predictive system that detects burnout risk before it impacts employee performance and retention.

---

## Dataset
The dataset includes employee-related information such as:

- Gender
- Company Type
- WFH Setup Available
- Designation
- Resource Allocation
- Mental Fatigue Score
- Burn Rate (Target Variable)
- Other employee-related features

### Target Variable
- **Burn Rate**

---

## Project Workflow

### 1. Data Collection
- Load and inspect the dataset.
- Understand the features and target variable.

### 2. Data Cleaning
- Handle missing values.
- Remove duplicate records.
- Correct data types.
- Detect and fix inconsistent values.

### 3. Exploratory Data Analysis (EDA)
- Analyze feature distributions.
- Explore relationships between variables.
- Visualize important trends.
- Identify factors affecting employee burnout.

### 4. Data Preprocessing
- Encode categorical variables.
- Scale numerical features.
- Split the dataset into training and testing sets.

### 5. Machine Learning Models
The project compares multiple regression models, including:

- Linear Regression
- Polynomial Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree Regressor
- Random Forest Regressor
- Bagging Regressor
- AdaBoost Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

### 6. Model Evaluation
Models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model was selected based on these metrics.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook

---

## Repository Structure

```
Employee-Burnout-Prediction/
│
├── Data/
│   ├── train.csv
│   └── test.csv
│
├── Notebooks/
│   └── Employee_Burnout_Prediction.ipynb
│
├── README.md
└── requirements.txt
```

---

## Results

The developed Machine Learning pipeline successfully predicts employee burnout levels by learning patterns from employee data.

This project demonstrates how predictive analytics can help organizations:

- Detect burnout early.
- Monitor employee wellbeing.
- Improve workforce planning.
- Support data-driven HR decisions.

---

## Team Members

This project was developed collaboratively by a team of five contributors.

| Team Member | Responsibilities |
|-------------|------------------|
| **Walaa Omar** | Data Cleaning, Linear Regression Model |
| **Esraa Sameh** | Data Preprocessing, Bagging, AdaBoost, Gradient Boosting, XGBoost |
| **Ziad Mohamed** | Exploratory Data Analysis (EDA), Polynomial Regression |
| **Mahmoud Fawzy** | K-Nearest Neighbors (KNN), Support Vector Machine (SVM) |
| **Youssef Tarek** | Decision Tree, Random Forest |

---

## Project Highlights

- Cleaned and prepared the employee burnout dataset.
- Performed Exploratory Data Analysis (EDA) to understand burnout patterns.
- Applied feature preprocessing techniques.
- Built and compared ten different Machine Learning regression models.
- Evaluated model performance using MAE, MSE, RMSE, and R² Score.
- Selected the best-performing model for burnout prediction.
- Demonstrated how Machine Learning can support early burnout detection and employee wellbeing.

---

## Future Improvements

- Hyperparameter tuning.
- Cross-validation.
- Feature selection.
- Explainable AI using SHAP.
- Deploy the model with Streamlit or Flask.
- Build an interactive HR dashboard.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/lool133/Employee-Burnout-Prediction.git
```

Navigate to the project folder:

```bash
cd Employee-Burnout-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook
```

---

## Author

**Walaa Omar**


---

## License

This project was developed for educational and portfolio purposes.
