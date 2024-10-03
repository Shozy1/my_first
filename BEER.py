import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def app():
    st.title("Behavioral Equilibrium Exchange Rate (BEER) Forecast")

    # Load the data
    data_url = "https://raw.githubusercontent.com/Shozy1/my_first/master/EXR.csv"
    df = pd.read_csv(data_url)

    # Select independent and dependent variables
    X = df[['INF_Nig', 'INF_US', 'NFA', 'COP', 'EXPT', 'IMPT']]
    y = df['EXR']

    # Handle missing values if needed
    X = X.fillna(0)
    y = y.fillna(0)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Convert X_train and y_train to NumPy arrays if they are not already
    X_train = X_train.values
    y_train = y_train.values

    # Fit a simple Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions and show results
    y_pred = model.predict(X_test)
    st.write("Model trained successfully!")
