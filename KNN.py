from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import pandas as pd
import numpy as np
from math import sqrt

# Load train and test data
train_data = pd.read_csv('data_train.csv')
test_data = pd.read_csv('data_test.csv')

# Feature engineering: Combine SSID and MAC address
train_data['SSID_MAC'] = train_data['SSID'] + '_' + train_data['MAC address']
test_data['SSID_MAC'] = test_data['SSID'] + '_' + test_data['MAC address']

# OneHotEncoding for SSID_MAC
from sklearn.preprocessing import OneHotEncoder
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

# Train KNN models for X and Y coordinates
k = 5  # Number of neighbors, adjustable
knn_model_x = KNeighborsRegressor(n_neighbors=k)
knn_model_x.fit(X_train, y_train_x)

knn_model_y = KNeighborsRegressor(n_neighbors=k)
knn_model_y.fit(X_train, y_train_y)

# Make predictions
knn_pred_x = knn_model_x.predict(X_test)
knn_pred_y = knn_model_y.predict(X_test)

# Save models and encoder
joblib.dump(knn_model_x, 'knn_model_x.pkl')
joblib.dump(knn_model_y, 'knn_model_y.pkl')
joblib.dump(encoder, 'knn_encoder.pkl')

# Calculate errors
mae_x_knn = mean_absolute_error(y_test_x, knn_pred_x)
mae_y_knn = mean_absolute_error(y_test_y, knn_pred_y)
rmse_x_knn = sqrt(mean_squared_error(y_test_x, knn_pred_x))
rmse_y_knn = sqrt(mean_squared_error(y_test_y, knn_pred_y))

# Print errors
print(f"KNN Model (k={k}):")
print(f"MAE: X={mae_x_knn:.4f}, Y={mae_y_knn:.4f}")
print(f"RMSE: X={rmse_x_knn:.4f}, Y={rmse_y_knn:.4f}")
