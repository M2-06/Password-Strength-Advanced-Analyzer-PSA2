import requests
import base64

# Define the function to make the API call
def check_password_hash(sha256):
    # Your Enzoic API Key and Secret
    api_key = "bc1277cf27444bea8d873591c4751e84"
    api_secret = "D&@XnC-@WrVDz^@=JcSF8hb7$XUJP8!V"

    # Combine and encode in Base64
    credentials = f"{api_key}:{api_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Set up headers with Basic Authentication
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }
    partial_sha256 = sha256[:10]
    print(partial_sha256)

    # Make the API call with partial SHA256
    response = requests.post(
        "https://api.enzoic.com/v1/passwords",
        headers=headers,
        json={"partialSHA256": partial_sha256}
    )

    # Check and handle the response
    if response.status_code == 200:
        data = response.json()
        if 'candidates' in data and data['candidates']:
            exposure_count = data['candidates'][0].get('exposureCount', 0)
            return exposure_count
        else:
            return 0
        
