from flask import Flask, jsonify, render_template, request
import time
import numpy as np
import joblib
import pandas as pd
import requests  # Import requests to make POST requests

app = Flask(__name__)

app = Flask(__name__)

# Store the latest coordinate
latest_coordinate = {'x': 0, 'y': 0}

# Load the saved Random Forest models and encoder
rf_model_x = joblib.load('rf_model_x.pkl')
rf_model_y = joblib.load('rf_model_y.pkl')
encoder = joblib.load('encoder.pkl')

@app.route('/')
def index():
    return render_template('index.html')  # Assumes index.html is in the templates folder

@app.route('/coordinates', methods=['GET', 'POST'])
def coordinates():
    global latest_coordinate
    if request.method == 'POST':
        # Update the coordinate with user-provided values
        data = request.json
        if 'x' in data and 'y' in data:
            latest_coordinate = {'x': data['x'], 'y': data['y']}
            return jsonify({"message": "Coordinate updated"}), 200
        return jsonify({"error": "Invalid data"}), 400
    # For GET requests, return the latest coordinate
    return jsonify(latest_coordinate)

@app.route('/upload_csv', methods=['POST'])
def upload_json():
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400

        # Filter routers based on SSID containing 'usth' or 'ict'
        filtered_data = [
            item for item in data 
            if 'usth' in item['ssid'].lower() or 'ict' in item['ssid'].lower()
        ]

        if not filtered_data:
            return jsonify({"error": "No valid routers found"}), 400

        # Extract routers and signal strengths from the filtered JSON object
        routers = [{'ssid': item['ssid'], 'bssid': item['macAddress']} for item in filtered_data]
        signal_strengths = [{'ssid': item['ssid'], 'signal': item['signalStrength']} for item in filtered_data]

        # Predict coordinates
        x_pred, y_pred = predict_coordinates(routers, signal_strengths)

        # Send the predicted coordinates to the /coordinates endpoint
        response = requests.post('http://localhost:5000/coordinates', json={'x': x_pred, 'y': y_pred})

        return jsonify({
            "predicted_coordinates": {"x": x_pred, "y": y_pred},
            "coordinates_update_response": response.json()
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
