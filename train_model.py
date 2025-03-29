from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import pandas as pd
import numpy as np

# Load train and test data
train_data = pd.read_csv('data_train.csv')
test_data = pd.read_csv('data_test.csv')

# Feature engineering: Combine SSID and MAC address
train_data['SSID_MAC'] = train_data['SSID'] + '_' + train_data['MAC address']
test_data['SSID_MAC'] = test_data['SSID'] + '_' + test_data['MAC address']

# OneHotEncoding for SSID_MAC
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_train = encoder.fit_transform(train_data[['SSID_MAC']])
encoded_test = encoder.transform(test_data[['SSID_MAC']])

# Prepare features and targets
X_train = np.hstack((encoded_train, train_data[['Signal Strength (dBm)']]))
X_test = np.hstack((encoded_test, test_data[['Signal Strength (dBm)']]))

y_train_x = train_data['X Position'].values
y_train_y = train_data['Y Position'].values
y_test_x = test_data['X Position'].values
y_test_y = test_data['Y Position'].values

# Train Linear Regression models for X and Y coordinates
lr_model_x = LinearRegression()
lr_model_x.fit(X_train, y_train_x)

lr_model_y = LinearRegression()
lr_model_y.fit(X_train, y_train_y)

# Make predictions
lr_pred_x = lr_model_x.predict(X_test)
lr_pred_y = lr_model_y.predict(X_test)

# Function to smooth predictions using a moving average
def smooth_predictions(predictions, window_size=3):
    '''
    Smooth predictions using a moving average filter.
    :param predictions: Array of predicted values.
    :param window_size: Size of the smoothing window (default is 3).
    :return: Smoothed predictions.
    '''
    return np.convolve(predictions, np.ones(window_size)/window_size, mode='same')

# Apply smoothing to predictions
window_size = 5  # Adjustable window size
lr_pred_x_smoothed = smooth_predictions(lr_pred_x, window_size=window_size)
lr_pred_y_smoothed = smooth_predictions(lr_pred_y, window_size=window_size)


# Save models and encoder
joblib.dump(lr_model_x, 'lr_model_x.pkl')
joblib.dump(lr_model_y, 'lr_model_y.pkl')
joblib.dump(encoder, 'lr_encoder.pkl')

# Calculate errors
mae_x_lr = mean_absolute_error(y_test_x, lr_pred_x)
mae_y_lr = mean_absolute_error(y_test_y, lr_pred_y)
rmse_x_lr = mean_squared_error(y_test_x, lr_pred_x, squared=False)
rmse_y_lr = mean_squared_error(y_test_y, lr_pred_y, squared=False)


