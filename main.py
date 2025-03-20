import requests
import json
import time
from datetime import datetime

# Jenga API Configuration
API_KEY = "PozKLVY8Sk30ERkEIX1i5mJwZ8uB282zKr8PiX9Oq7sp2QxVkWkkPcvslDzE/51xgzckZPe4S3rHg+KICvHcEQ=="
MERCHANT_CODE = "8555151323"
CONSUMER_SECRET = "Bz4wADSSf37URef8lx9c13T992xCkD"
AUTH_URL = "https://uat.finserve.africa/authentication/api/v3/authenticate/merchant"
TOKEN_FILE = "token.json"

def get_auth_token():
    headers = {
        "Api-Key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "merchantCode": MERCHANT_CODE,
        "consumerSecret": CONSUMER_SECRET
    }

    try:
        response = requests.post(AUTH_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        token = data.get("accessToken")
        if not token:
            print("No access token received in response")
            print("Auth Response:", data)
            return None
        return token
    except requests.exceptions.RequestException as e:
        print(f"Authentication failed: {str(e)}")
        if e.response is not None:
            print("Auth Response:", e.response.text)
        return None

def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        json.dump({"token": token}, f)

def refresh_token():
    token = get_auth_token()
    if token:
        save_token(token)
        print(f"Token refreshed at {datetime.now()}")
    else:
        print("Failed to refresh token")

if __name__ == "__main__":
    # Initial token fetch
    refresh_token()

    # Schedule token refresh every 15 minutes
    while True:
        time.sleep(900)  # 15 minutes in seconds
        refresh_token()
