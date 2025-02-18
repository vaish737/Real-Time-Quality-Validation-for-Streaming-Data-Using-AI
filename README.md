# Real-Time Quality Validation for Streaming Data Using AI

## Project Overview

**Real-Time Quality Validation for Streaming Data Using AI** is a project that leverages Artificial Intelligence (AI) techniques to validate the quality of streaming data in real time. In this project, we focus on **weather data streaming** as a use case, simulating real-time data collection for weather parameters such as temperature, humidity, and pressure from various sensors.

Ensuring the accuracy and reliability of this constantly generated weather data is critical, especially for decision-making in sectors like **agriculture**, **transportation**, and **disaster management**.

The project integrates **AI-based anomaly detection** using the **Isolation Forest** model to identify outliers in real-time data streams. As new data arrives, it undergoes preprocessing, validation, and anomaly detection. The validated data is continuously displayed in a **Streamlit dashboard** for real-time monitoring.

### **Key Features**
- **Simulated Weather Data Stream**: Data such as temperature, humidity, and pressure is continuously generated in real-time.
- **AI-Based Anomaly Detection**: The project uses the **Isolation Forest** model to detect anomalies in the data.
- **Real-Time Data Validation**: Incoming data is validated for consistency and reliability.
- **Interactive Dashboard**: A **Streamlit** dashboard displays the data trends and anomaly detection results.

## Use Case: Real-Time Weather Data Streaming and Quality Validation

In this system, we chose **weather data streaming** to demonstrate the power of AI-driven real-time data validation. Weather data, including parameters like temperature, humidity, and pressure, is generated continuously from various sensors. Ensuring that this data is reliable is essential for accurate forecasts and decision-making across multiple sectors.

The system integrates **AI-based anomaly detection** using the **Isolation Forest** model to monitor the streaming data. Each new data point undergoes preprocessing and validation to detect any anomalous values. The validated data is displayed on a **real-time dashboard**, which provides insights into data trends and anomalies.

## Project Steps

### 1. Setup the Environment

- **Install Python 3.x**: Ensure Python 3.6 or higher is installed on your system.
  
- **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

- **Install Required Libraries**:
    Create a `requirements.txt` file with the following content:
    ```txt
    streamlit==1.18.0
    pandas==1.5.3
    scikit-learn==1.2.0
    ```

    Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Create the Main Application (app.py)

The core application (app.py) includes:

- **Title & Description**: Display the title and description of the project using Streamlit.
- **Data Simulation**: Simulate real-time weather data stream, including temperature, humidity, and pressure.
- **Preprocessing**: Clean and preprocess the data by handling missing values and ensuring the data is within valid ranges.
- **AI Model (Isolation Forest)**: Use **Isolation Forest** to train a model for detecting anomalies in the data.
- **Real-Time Dashboard**: Display incoming data and trends using Streamlit.
- **Anomaly Detection**: Flag any outlier data points as anomalies.

### 3. Implement Anomaly Detection

- **Train Isolation Forest**: Use `scikit-learn`'s **Isolation Forest** model to detect outliers in the data.
- **Data Validation**: For each new data point, check if it is an anomaly and mark it accordingly.

### 4. Real-Time Data Processing

- **Simulate Data**: Continuously generate and preprocess new data.
- **Validate**: Use the trained AI model to validate data and classify it as **Valid** or **Anomaly**.
- **Display**: Use **Streamlit** to dynamically display the data and detected anomalies.

### 5. Run the Application

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
