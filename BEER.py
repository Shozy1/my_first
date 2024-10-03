import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def app():
    st.title("Behavioral Equilibrium Exchange Rate (BEER) Forecast")

    st.write("""
        The **Behavioral Equilibrium Exchange Rate (BEER)** model forecasts exchange rates using macroeconomic variables like:
        - Inflation Rates
        - Interest Rates
        - Net Foreign Assets (NFA)
        - Crude Oil Prices
    """)

    # Load the data
    data_url = "https://raw.githubusercontent.com/Shozy1/my_first/master/EXR.csv"
    df = pd.read_csv(data_url)

    # Preprocess data (you can adjust this to your own dataset)
    st.subheader("Data Preview")
    st.write(df.head())

    # Select independent and dependent variables for modeling
    X = df[['INF_Nig', 'INF_US', 'NFA', 'COP', 'EXPT', 'IMPT']]  # Features (adjust based on your data)
    y = df['EXR']  # Dependent variable (exchange rate)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train = X_train.select_dtypes(include=[np.number])  # Select only numeric columns
    y_train = y_train.astype(float)  # Convert target column to numeric

    X_train = X_train.dropna()  # Dropping rows with missing values
    y_train = y_train.dropna()
    # Train a simple Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Display model performance
    st.subheader("Model Performance")
    st.write("Mean Squared Error: ", mean_squared_error(y_test, y_pred))
    
    # Input features for forecasting
    st.sidebar.subheader("Input Features for Forecasting")
    INF_Nig = st.sidebar.slider('Inflation Rate in Nigeria', 0.1, 50.0, 25.0)
    INF_US = st.sidebar.slider('Inflation Rate in the US', 0.1, 20.0, 10.0)
    NFA = st.sidebar.slider('Net Foreign Asset', 5000000, 30000000, 10000000)
    COP = st.sidebar.slider('Crude Oil Price', 10, 300, 150)
    EXPT = st.sidebar.slider('Export', 500000, 30000000, 12000000)
    IMPT = st.sidebar.slider('Import', 500000, 30000000, 12000000)

    # Create a DataFrame from the input
    input_data = {
        'INF_Nig': [INF_Nig],
        'INF_US': [INF_US],
        'NFA': [NFA],
        'COP': [COP],
        'EXPT': [EXPT],
        'IMPT': [IMPT]
    }
    input_df = pd.DataFrame(input_data)

    # Make prediction based on the input features
    forecast = model.predict(input_df)

    st.subheader("Forecasted Exchange Rate")
    st.write(f"The forecasted exchange rate is: {forecast[0]:.2f}")
