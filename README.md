# ❤️ Heart Disease Prediction using Linear Regression
Heart disease prediction using Linear Regression to explore model behavior on a classification problem and analyze bias–variance tradeoffs.

---

## 📌 Project Overview

This project explores the use of Linear Regression for predicting the presence of heart disease.

Although heart disease prediction is fundamentally a classification problem, this experiment intentionally uses Linear Regression to evaluate:

How well a regression model can approximate a binary outcome

The bias–variance tradeoff in linear models

Model limitations when applied outside their ideal problem domain

While models like Decision Tree Classifier or Logistic Regression would typically perform better (lower bias and better handling of non-linearity), this project investigates how far a simple linear model can go.

---

## 🎯 Objective

Apply Linear Regression to a binary classification problem

Evaluate performance using regression and classification metrics

Understand why more flexible models (e.g., Decision Trees) may outperform linear models in this domain

Analyze bias–variance behavior

---

## 📊 Dataset

The dataset contains medical attributes such as:

Age

Sex

Chest Pain Type

Resting Blood Pressure

Cholesterol

Fasting Blood Sugar

Maximum Heart Rate

Exercise Induced Angina

ST Depression

Number of Major Vessels

Thalassemia

Target (0 = No Disease, 1 = Disease)

---

## 🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

Seaborn

---

## ⚙️ Methodology

Data Preprocessing

Handling missing values

Feature scaling using StandardScaler

Train-test split

Model Used

LinearRegression() from Scikit-learn

Evaluation

R² Score

Mean Squared Error

Thresholding predictions for classification evaluation

---

## 📈 Why Linear Regression?

Heart disease prediction is a classification problem, so models like:

Logistic Regression

Decision Tree Classifier

Random Forest

Gradient Boosting

would normally perform better.

However, this project tests:

Whether a linear relationship approximates disease prediction

How regression behaves when used for classification

The trade-off between model simplicity and predictive power

This helps build intuition about model assumptions and their impact.

---

## 📉 Observations

Linear Regression struggles with non-linear boundaries.

Predictions may fall outside [0, 1], requiring thresholding.

Higher bias compared to tree-based models.

Provides a good baseline for comparison.
<img width="1918" height="916" alt="image" src="https://github.com/user-attachments/assets/04524475-406c-4479-9c63-0df4d2e5f741" />
<img width="1918" height="911" alt="image" src="https://github.com/user-attachments/assets/3da3968d-41f5-4c1e-8aaa-d8dd3f27501f" />
<img width="1918" height="901" alt="image" src="https://github.com/user-attachments/assets/09014f48-3a3d-46df-a5cb-19f75a5e9941" />

---

## 🚀 Future Improvements

Implement Decision Tree Classifier

Compare with Logistic Regression

Use Random Forest for better generalization

Perform hyperparameter tuning

Add ROC-AUC evaluation

---
