import requests
import base64

# Combine API Key and Secret
api_key = "bc1277cf27444bea8d873591c4751e84"
api_secret = "D&@XnC-@WrVDz^@=JcSF8hb7$XUJP8!V"
credentials = f"{api_key}:{api_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(
    "https://api.enzoic.com/v1/passwords",
    headers=headers,
    json={"partialSHA256": "9f86d08188"}
)

# Handle the response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)
