import requests
import pandas as pd
import io

# Create example router data
data = {
    "SSID": ["USTH_Guest", "USTH_MGMT", "USTH_Office", "USTH_Student"],
    "Signal Strength (dBm)": [-82, -81, -41, -49],
    "MAC Address": [
        "48:9b:d5:c5:67:82",
        "48:9b:d5:c5:67:83",
        "48:9b:d5:c5:67:80",
        "48:9b:d5:c5:67:81"
    ]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV in memory
csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)
csv_buffer.seek(0)

# Send the CSV data to the Flask app
url = 'http://192.168.103.114:5000/upload_csv'  # Adjust the URL if necessary
files = {'file': ('routers.csv', csv_buffer.getvalue())}

response = requests.post(url, files=files)

# Print the response from the server
print(response.json())
