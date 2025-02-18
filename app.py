import streamlit as st
import random
import pandas as pd
from sklearn.ensemble import IsolationForest
import time

# Title and Abstract Display
st.title("Real-Time Quality Validation for Streaming Data Using AI")
st.markdown("""

#### **Use Case: Real-Time Weather Data Streaming and Quality Validation**

In this System, we chose the **weather data streaming** use case to demonstrate the power of AI-driven real-time data validation. Weather data, such as temperature, humidity, pressure, wind speed, and air quality, is constantly generated from various sensors and meteorological stations worldwide. Ensuring the quality and reliability of this streaming data is critical for making accurate forecasts, timely warnings, and informed decisions across various sectors like agriculture, transportation, and disaster management.

To address this, our system integrates **AI-based anomaly detection** using the **Isolation Forest** model. The system simulates the streaming of weather data in real-time, and as new data arrives, it undergoes preprocessing, validation, and anomaly detection to identify any unusual or unreliable values. The validated data is stored and continuously displayed in a **real-time dashboard** to allow monitoring and analysis.

By applying this real-time data validation system to weather data, we ensure that only trustworthy and consistent data is used, which is essential for critical decision-making processes in various fields.
""")

# Initialize Session State for Data Storage
if "historical_data" not in st.session_state:
    st.session_state.historical_data = pd.DataFrame(columns=["temperature", "humidity", "pressure", "status"])

# Simulated Data Stream Function
def generate_data():
    return {
        "temperature": random.uniform(-10, 50),
        "humidity": random.uniform(0, 100),
        "pressure": random.uniform(900, 1100)
    }

# Data Preprocessing
def preprocess_data(data):
    df = pd.DataFrame([data])
    df["temperature"] = df["temperature"].clip(-10, 50)  # Boundary for valid temperature
    df["humidity"] = df["humidity"].fillna(50)  # Default value for missing humidity
    df["pressure"] = df["pressure"].fillna(1000)  # Default value for missing pressure
    return df

# Initialize AI Model
@st.cache_resource
def initialize_model():
    training_data = pd.DataFrame({
        "temperature": [random.uniform(-10, 50) for _ in range(1000)],
        "humidity": [random.uniform(0, 100) for _ in range(1000)],
        "pressure": [random.uniform(900, 1100) for _ in range(1000)],
    })
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(training_data)
    return model

# AI-Based Validation
def validate_data(model, data):
    if isinstance(data, pd.DataFrame):
        df = data  # If already a DataFrame, use it directly
    else:
        df = pd.DataFrame([data])  # Convert to DataFrame only if needed
    
    prediction = model.predict(df)[0]
    return "Valid" if prediction == 1 else "Anomaly"


# Initialize Model
st.write("Initializing the anomaly detection model...")
model = initialize_model()
st.success("Model initialized successfully!")

# Streaming Data with Real-Time Validation
st.write("### Real-Time Data Quality Monitoring")
placeholder = st.empty()

while True:
    # Generate & preprocess incoming data
    raw_data = generate_data()
    processed_data = preprocess_data(raw_data)

    # Validate data using the AI model
    status = validate_data(model, processed_data)
    processed_data["status"] = status

    # Update historical data
    st.session_state.historical_data = pd.concat([st.session_state.historical_data, processed_data], ignore_index=True)

    # Display Data in Streamlit UI
    with placeholder.container():
        st.write("#### Latest Data with Validation Status")
        st.dataframe(st.session_state.historical_data.tail(10))

        st.write("#### Data Trends Over Time")
        st.line_chart(st.session_state.historical_data[["temperature", "humidity", "pressure"]])

        st.write("#### Recent Anomalies")
        anomalies = st.session_state.historical_data[st.session_state.historical_data["status"] == "Anomaly"].tail(5)
        if not anomalies.empty:
            st.dataframe(anomalies)
        else:
            st.write("No anomalies detected in recent data.")

    # Pause to simulate real-time streaming
    time.sleep(2)
