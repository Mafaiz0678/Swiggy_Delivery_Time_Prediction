import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load Trained Pipeline
# -----------------------------
with open("swiggy_delivery_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Swiggy Delivery Time Prediction",
    page_icon="🛵",
    layout="wide"
)

st.title("🛵 Swiggy Delivery Time Prediction")
st.markdown("Predict the estimated delivery time for a Swiggy order.")

st.sidebar.header("Enter Order Details")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input("Delivery Partner Age",18,60,30)

    ratings = st.number_input("Ratings",1.0,5.0,4.5,step=0.1)

    weather = st.selectbox(
        "Weather",
        ["cloudy","fog","sandstorms","stormy","sunny","windy"]
    )

    traffic = st.selectbox(
        "Traffic",
        ["low","medium","high","jam"]
    )

    vehicle_condition = st.selectbox(
        "Vehicle Condition",
        [0,1,2]
    )

    type_of_order = st.selectbox(
        "Order Type",
        ["buffet","drinks","meal","snack"]
    )

    type_of_vehicle = st.selectbox(
        "Vehicle Type",
        ["bicycle","electric_scooter","motorcycle","scooter"]
    )

    multiple_deliveries = st.selectbox(
        "Multiple Deliveries",
        [0,1,2,3]
    )

    festival = st.selectbox(
        "Festival",
        ["no","yes"]
    )

    city_type = st.selectbox(
        "City Type",
        ["metropolitian","semi-urban","urban"]
    )

with col2:

    city_name = st.selectbox(
        "City",
        [
            "AGR","ALH","AURG","BANG","BHP","CHEN",
            "COIMB","DEH","GOA","HYD","INDO","JAP",
            "KNP","KOC","KOL","LUDH","MUM","MYS",
            "PUNE","RANCHI","SUR","VAD"
        ]
    )

    order_day = st.slider("Order Day",1,31,15)

    order_month = st.slider("Order Month",1,12,6)

    order_day_of_week = st.selectbox(
        "Day of Week",
        [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday"
        ]
    )

    is_weekend = st.selectbox(
        "Weekend",
        [0,1]
    )

    pickup_time_minutes = st.number_input(
        "Pickup Time (minutes)",
        min_value=0.0,
        value=15.0
    )

    order_time_hour = st.slider(
        "Order Hour",
        0,
        23,
        12
    )

    order_time_of_day = st.selectbox(
        "Time of Day",
        [
            "after_midnight",
            "morning",
            "afternoon",
            "evening",
            "night"
        ]
    )

    distance = st.number_input(
        "Distance (km)",
        min_value=0.1,
        value=5.0
    )

    Peak_Hour = st.selectbox(
        "Peak Hour",
        [0,1]
    )

    Delivery_Load = st.selectbox(
        "Delivery Load",
        ["Low","High"]
    )

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Delivery Time"):

    input_data = pd.DataFrame({

        "age":[age],
        "ratings":[ratings],
        "weather":[weather],
        "traffic":[traffic],
        "vehicle_condition":[vehicle_condition],
        "type_of_order":[type_of_order],
        "type_of_vehicle":[type_of_vehicle],
        "multiple_deliveries":[multiple_deliveries],
        "festival":[festival],
        "city_type":[city_type],
        "city_name":[city_name],
        "order_day":[order_day],
        "order_month":[order_month],
        "order_day_of_week":[order_day_of_week],
        "is_weekend":[is_weekend],
        "pickup_time_minutes":[pickup_time_minutes],
        "order_time_hour":[order_time_hour],
        "order_time_of_day":[order_time_of_day],
        "distance":[distance],
        "Peak_Hour":[Peak_Hour],
        "Delivery_Load":[Delivery_Load]

    })

    prediction = model.predict(input_data)

    st.success(f"🚀 Estimated Delivery Time: {prediction[0]:.2f} minutes")