# Sources:
# https://blog.goodaudience.com/using-the-twitter-api-with-python-c6e8da96d273

import base64
import requests

# Consumer API keys
# TODO: use .env file: https://pypi.org/project/python-dotenv/
API_KEY = 'RV8lBpxB7hiezPVK2HwM6KNPy'
API_SECRET_KEY = 'gKaAsAP1BUWikumjpJ4MZM0JeLIjgwBqBTkfNYuIgUzPFkNZGM'

# Formatting
key_ascii = '{}:{}'.format(API_KEY, API_SECRET_KEY).encode('ascii')
key_base64 = base64.b64encode(key_ascii)
key_base64 = key_base64.decode('ascii')

# Request
base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
  'Authorization': 'Basic {}'.format(key_base64),
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
  'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
print(auth_resp.status_code)
