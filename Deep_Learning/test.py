# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns  # For loading the dataset
from sklearn.preprocessing import MinMaxScaler  # For normalizing data
from sklearn.metrics import mean_squared_error, mean_absolute_error
# import tensorflow as tf
# from tensorflow import keras
from keras.src.models.sequential import Sequential
from keras.src.layers.core.dense import Dense
from keras.src.layers.rnn.lstm import LSTM
# from k.models import Sequential  # For creating the LSTM model
# from k.layers import LSTM, Dense  # For adding LSTM and Dense layers
import matplotlib.pyplot as plt  # For plotting the results


# Load the 'tips' dataset from seaborn
data = sns.load_dataset('tips')

# Take the 'total_bill' column as a pseudo-stock price for the demo
prices = data['total_bill'].values.reshape(-1,1)  # Reshape to a 2D array for scaling

print("Prices : ", prices)

# Normalize the data using MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(prices)  # Scale data between 0 and 1

print("Scaled Data : ",scaled_data)


# print("prices : ",type(prices))
# print("Scaled Data : ",type(scaled_data))
# df = pd.DataFrame(prices)
# print(df.head(5))


# Create the training data by taking past 'time_step' values to predict the next one
train_data = []
target_data = []
time_step = 10  # Using past 10 values to predict the next one

# Loop through the scaled data and prepare input-output sequences
for i in range(time_step, len(scaled_data)):
    train_data.append(scaled_data[i-time_step:i, 0])  # Last 10 days
    target_data.append(scaled_data[i, 0])  # Next day (target)

train_data, target_data = np.array(train_data), np.array(target_data)
train_data = np.reshape(train_data, (train_data.shape[0], train_data.shape[1], 1))  # Reshape for LSTM input


# Build the LSTM model
model = Sequential()

# Add the first LSTM layer with 50 units (neurons) and return sequences to feed into the next LSTM layer
model.add(LSTM(units=50, return_sequences=True, input_shape=(train_data.shape[1], 1)))

# Add another LSTM layer without returning sequences
model.add(LSTM(units=50))

# Add a Dense output layer with 1 unit (for predicting the next value)
model.add(Dense(1))

# Compile the model using Adam optimizer and mean squared error as the loss function
model.compile(optimizer='adam', loss='mean_squared_error')


# Train the model for 10 epochs with a batch size of 32
model.fit(train_data, target_data, epochs=10, batch_size=32)

# Predict the future values based on training data
predicted_prices = model.predict(train_data)

# Inverse transform the predicted prices to the original scale
predicted_prices = scaler.inverse_transform(predicted_prices)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(target_data, predicted_prices)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(target_data, predicted_prices)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)

# Print the calculated metrics
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Plot the actual vs predicted values for visualization
plt.figure(figsize=(10,6))
plt.plot(prices, label='Actual Prices')  # Plot actual values
plt.plot(np.concatenate([np.zeros(time_step), predicted_prices.flatten()]), label='Predicted Prices')  # Plot predicted values
plt.legend()
plt.savefig('Deep_Learning/DL_Plots/LSTM_Plot.jpg')
plt.show()

