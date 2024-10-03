import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def app():
    # Assuming `data` is the full DataFrame loaded earlier
    global data

    # Data cleaning: remove non-numeric columns if any exist
    X = data.drop(columns=['EXR'], axis=1)  # Drop target column from features
    y = data['EXR']  # Target column

    # Handle missing values by filling them or dropping rows with missing values
    X = X.fillna(0)  # Filling missing values with 0, you can use other strategies
    y = y.fillna(0)

    # Convert to NumPy arrays to avoid DataFrame issues
    X = X.values
    y = y.values

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model (e.g., Linear Regression)
    model = LinearRegression()
    
    # Ensure both X_train and y_train are properly shaped
    print("X_train shape:", X_train.shape)  # Should be (n_samples, n_features)
    print("y_train shape:", y_train.shape)  # Should be (n_samples,)

    # Train the model
    model.fit(X_train, y_train)

    # Forecasting (or prediction)
    y_pred = model.predict(X_test)
    
    # Display results
    st.write("Model Predictions:", y_pred)
    st.write("Actual Values:", y_test)
