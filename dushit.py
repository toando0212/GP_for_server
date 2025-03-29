from flask import Flask, jsonify, render_template, request
import time
import numpy as np
import joblib
import pandas as pd
import requests  # Import requests to make POST requests

app = Flask(__name__)

# app = Flask(__name__)

# Store the latest predicted and actual coordinates
latest_coordinates = {
    'predicted': {'x': 0, 'y': 0},  # Vị trí dự đoán từ mô hình
    'actual': {'x': None, 'y': None}  # Vị trí chính xác từ mobile (mặc định là None)
}

# Load the saved Random Forest models and encoder
rf_model_x = joblib.load('svr_model_x.pkl')
rf_model_y = joblib.load('svr_model_y.pkl')
encoder = joblib.load('svr_encoder.pkl')

@app.route('/')
def index():
    return render_template('index.html')  # Assumes index.html is in the templates folder

@app.route('/coordinates', methods=['GET', 'POST'])
def coordinates():
    global latest_coordinates
    if request.method == 'POST':
        # Update the predicted coordinate with values from the model
        data = request.json
        if 'x' in data and 'y' in data:
            latest_coordinates['predicted'] = {'x': data['x'], 'y': data['y']}
            return jsonify({"message": "Predicted coordinate updated"}), 200
        return jsonify({"error": "Invalid data"}), 400
    # For GET requests, return both predicted and actual coordinates
    return jsonify(latest_coordinates)

@app.route('/upload_actual_coordinates', methods=['POST'])
def upload_actual_coordinates():
    global latest_coordinates
    if request.method == 'POST':
        # Get the JSON data from the request (actual coordinates from mobile)
        data = request.json
        if 'x' in data and 'y' in data:
            try:
                # Chuyển đổi tọa độ thành float để đảm bảo định dạng
                x = float(data['x'])
                y = float(data['y'])
                latest_coordinates['actual'] = {'x': x, 'y': y}
                return jsonify({"message": "Actual coordinate updated"}), 200
            except (ValueError, TypeError):
                return jsonify({"error": "Invalid coordinate values"}), 400
        return jsonify({"error": "Invalid data"}), 400
    return jsonify({"error": "Invalid request method"}), 405
@app.route('/upload_csv', methods=['POST'])
def upload_json():
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400

        # Check if the data is a coordinate (from "Send Coordinates" button)
        if 'x' in data and 'y' in data:
            # Update actual coordinates
            try:
                x = float(data['x'])
                y = float(data['y'])
                latest_coordinates['actual'] = {'x': x, 'y': y}
                return jsonify({"message": "Actual coordinate updated"}), 200
            except (ValueError, TypeError):
                return jsonify({"error": "Invalid coordinate values"}), 400

        # Otherwise, process Wi-Fi data for prediction
        # Filter routers based on SSID containing 'usth' or 'ict'
        filtered_data = [
            item for item in data
            if 'ssid' in item and 'macAddress' in item and 'signalStrength' in item
            and ('usth' in item['ssid'].lower() or 'ict' in item['ssid'].lower())
        ]

        if not filtered_data:
            return jsonify({"error": "No valid routers found"}), 400

        # Extract routers and signal strengths from the filtered JSON object
        routers = [{'ssid': item['ssid'], 'bssid': item['macAddress']} for item in filtered_data]
        signal_strengths = [{'ssid': item['ssid'], 'signal': item['signalStrength']} for item in filtered_data]

        # Predict coordinates
        x_pred, y_pred = predict_coordinates(routers, signal_strengths)

        # Update the predicted coordinates
        latest_coordinates['predicted'] = {'x': x_pred, 'y': y_pred}

        return jsonify({
            "predicted_coordinates": {"x": x_pred, "y": y_pred}
        }), 200

    return jsonify({"error": "Invalid request method"}), 405

# Function to predict coordinates based on signal strengths
def predict_coordinates(routers, networks):
    # Create SSID_MAC for the selected routers
    ssid_mac_list = []
    router_signals = []

    for router in routers:
        ssid_mac = f"{router['ssid']}_{router['bssid']}"  # Combine SSID and MAC address
        ssid_mac_list.append(ssid_mac)

        # Find the corresponding signal strength for the router
        signal_strength = next(
            (network['signal'] for network in networks if network['ssid'] == router['ssid']),
            0,  # Default to 0 if the network is not found
        )
        router_signals.append(signal_strength)

    # Encode SSID_MAC using the encoder
    encoded_ssid_mac = encoder.transform(np.array(ssid_mac_list).reshape(-1, 1))

    # Combine encoded SSID_MAC with signal strengths for prediction
    input_data = np.hstack((encoded_ssid_mac, np.array(router_signals).reshape(-1, 1)))

    # Predict the X and Y coordinates using the trained Random Forest models
    x_pred = rf_model_x.predict(input_data)
    y_pred = rf_model_y.predict(input_data)

    return x_pred[0], y_pred[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
