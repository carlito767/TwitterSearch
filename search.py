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

# Authentication
base_url = 'https://api.twitter.com/'

auth_headers = {
    'Authorization': 'Basic {}'.format(key_base64),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
auth_data = {
    'grant_type': 'client_credentials'
}
auth_url = '{}oauth2/token'.format(base_url)
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
print(f"Authentication status: {auth_resp.status_code}")

# Search
access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}
search_params = {
    'q': 'NASA',
    'result_type': 'recent',
    'count': 2
}
search_url = '{}1.1/search/tweets.json'.format(base_url)
search_resp = requests.get(search_url, headers=search_headers, params=search_params)
print(f"Search status: {search_resp.status_code}")
