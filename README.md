# 🛵 Swiggy Delivery Time Prediction

## 📌 Project Overview

This project predicts the estimated delivery time of Swiggy food orders using Machine Learning. It analyzes various factors such as delivery partner details, weather conditions, traffic, order information, city, and distance to estimate the delivery duration accurately.

The project includes complete data preprocessing, feature engineering, model building, hyperparameter tuning, deployment using Streamlit, and a trained machine learning pipeline.

---

## 🎯 Problem Statement

Food delivery companies need accurate delivery time predictions to improve customer satisfaction and optimize delivery operations.

This project develops a machine learning model that predicts delivery time based on order, delivery partner, weather, traffic, and location-related features.

---

## 📂 Dataset Features

The final model uses the following input features:

- Age
- Ratings
- Weather
- Traffic
- Vehicle Condition
- Type of Order
- Type of Vehicle
- Multiple Deliveries
- Festival
- City Type
- City Name
- Order Day
- Order Month
- Order Day of Week
- Is Weekend
- Pickup Time (Minutes)
- Order Time Hour
- Order Time of Day
- Distance
- Peak Hour
- Delivery Load

### Target Variable

- Time Taken (minutes)

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Pickle

---

## 📊 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Selection
6. Model Building
7. Hyperparameter Tuning
8. Pipeline Creation
9. Model Evaluation
10. Streamlit Deployment

---

## 🤖 Machine Learning Model

The final deployed model uses:

- XGBoost Regressor

Performance was improved using:

- Data Preprocessing Pipeline
- Hyperparameter Tuning (RandomizedSearchCV)
- Cross Validation

---

## 📁 Project Structure

```
Swiggy_Delivery_Time_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── swiggy_delivery_pipeline.pkl
├── swiggy_cleaned_dataset.csv
└── Swiggy Delivery Time Prediction_Project.ipynb
```

---

## ▶️ Run the Project

### Clone the repository

```bash
git clone <repository_url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📈 Features

- Interactive Streamlit Web Application
- User-friendly Interface
- Real-time Delivery Time Prediction
- Complete Machine Learning Pipeline
- Automatic Data Preprocessing
- XGBoost Regression Model

---

## 📸 Application

The application allows users to:

- Enter delivery details
- Provide order information
- Select weather and traffic conditions
- Predict estimated delivery time instantly

---

## 🚀 Future Improvements

- Live Google Maps Distance Integration
- Real-time Weather API
- Traffic API Integration
- Restaurant Location Mapping
- Delivery Route Optimization

---

## 👨‍💻 Author

**Mohammed Mafaizuddin**

Artificial Intelligence & Machine Learning Enthusiast

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.