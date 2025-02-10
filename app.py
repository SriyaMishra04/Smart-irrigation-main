import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load the saved model
model_file = 'linear_regression_model.joblib'
model = joblib.load(model_file)

# Define a function to predict water usage
def predict_water_usage(features):
    try:
        # Predict using the loaded model
        water_usage_prediction = model.predict(features)
        return water_usage_prediction
    except Exception as e:
        st.error(f"Error in prediction: {e}")
        return None

# Streamlit app begins
st.title('Water Usage Prediction App')

# Sidebar for input features
st.sidebar.header('Input Features')

# Example input fields (replace with actual user input or sliders)
default_input = {
     'SoilMoisture': 0.3,
    'SoilTemperature': 20.0,
    'AirTemperature': 25.0,
    'Humidity': 0.5,
    'pH': 6.5,
    'CropType': 1.0,  # Assuming CropType is encoded as numerical values
    'SolarRadiation': 300.0,
    'WindSpeed': 5.0
}
# Collect user input through sidebar
user_input = {}
for key, value in default_input.items():
    user_input[key] = st.sidebar.number_input(key, value=value)

# Function to predict and display water usage on button click
if st.sidebar.button('Predict Water Usage'):
    # Convert user input into DataFrame
    input_features = pd.DataFrame([user_input])

    # Make prediction
    predicted_water_usage = predict_water_usage(input_features)

    # Display prediction if no error
    if predicted_water_usage is not None:
        st.write('## Predicted Water Usage')
        st.write(f'The predicted water usage is {predicted_water_usage[0]:.2f} units')

# Optional: Display additional information or the dataset (if needed for context)
# st.subheader("Dataset")
# st.write(final_df)
