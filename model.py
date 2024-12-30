import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

train_data = pd.read_csv('data_train.csv')
test_data = pd.read_csv('data_test.csv')

train_data['SSID_MAC'] = train_data['SSID'] + '_' + train_data['MAC address']
test_data['SSID_MAC'] = test_data['SSID'] + '_' + test_data['MAC address']

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_train = encoder.fit_transform(train_data[['SSID_MAC']])
encoded_test = encoder.transform(test_data[['SSID_MAC']])

X_train = np.hstack((encoded_train, train_data[['Signal Strength (dBm)']]))
X_test = np.hstack((encoded_test, test_data[['Signal Strength (dBm)']]))

y_train_x = train_data['X Position']
y_train_y = train_data['Y Position']
y_test_x = test_data['X Position']
y_test_y = test_data['Y Position']

rf_model_x = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_model_x.fit(X_train, y_train_x)

rf_model_y = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_model_y.fit(X_train, y_train_y)

rf_pred_x = rf_model_x.predict(X_test)
rf_pred_y = rf_model_y.predict(X_test)

