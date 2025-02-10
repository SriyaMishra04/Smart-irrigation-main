import streamlit as st
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
@st.cache
def load_data():
    final_df = pd.read_xlsx('enhanced_iot_smart_irrigation_data.xlsx')
    return final_df

final_df = load_data()

# Prepare X and y
X = final_df.drop(['WaterUsage', 'ReadingTimestamp', 'IrrigationSystemID'], axis=1)
y = final_df['WaterUsage']

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
reg = linear_model.LinearRegression()
reg.fit(xtrain, ytrain)
pred = reg.predict(xtest)

# Calculate metrics
acc = r2_score(ytest, pred)
rms = mean_squared_error(ytest, pred, squared=False)
MSE = np.square(np.subtract(ytest, pred)).mean()

# Display the metrics in the Streamlit app
st.title("Linear Regression Model for Water Usage Prediction")

st.write(f"**R² Score:** {acc}")
st.write(f"**Root Mean Squared Error (RMSE):** {rms}")
st.write(f"**Mean Squared Error (MSE):** {MSE}")

# Plot the results
st.subheader("Prediction vs Actual")

fig, ax = plt.subplots()
sns.scatterplot(x=ytest, y=pred, ax=ax)
ax.set_xlabel('Actual Water Usage')
ax.set_ylabel('Predicted Water Usage')
ax.set_title('Actual vs Predicted Water Usage')

st.pyplot(fig)

# Display the dataset
st.subheader("Dataset")
st.write(final_df)
