import requests
import pandas as pd

# Load the CSV file
csv_path = "example_routers.csv"  # Ensure this matches your CSV file path
df = pd.read_csv(csv_path)

# Convert the DataFrame to JSON format
data_json = df.to_dict(orient='records')

# Define the Flask server endpoint
url = "http://127.0.0.1:5000/upload_csv"  # Replace with your server's URL if deployed

# Post the JSON data to the Flask server
response = requests.post(url, json=data_json)

# Print the server's response
print("Status Code:", response.status_code)
print("Response:", response.json())

