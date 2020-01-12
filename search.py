# Sources:
# https://blog.goodaudience.com/using-the-twitter-api-with-python-c6e8da96d273
# https://preslav.me/2019/01/09/dotenv-files-python/

import base64
import json
import os
import requests
import webbrowser

# Settings
from dotenv import load_dotenv
load_dotenv()

# Consumer API keys
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

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
    'count': 1
}
search_url = '{}1.1/search/tweets.json'.format(base_url)
search_resp = requests.get(search_url, headers=search_headers, params=search_params)
print(f"Search status: {search_resp.status_code}")

data = json.loads(search_resp.content)
tweet_id = data['statuses'][0]['id']
print(f"Tweet Id: {tweet_id}")

# JSON file
# TODO: use unique filename
file = open("out.json", "w+")
json.dump(data, file)
file.close()

# Tweet in default browser
tweet_url = f"twitter.com/user/status/{tweet_id}"
webbrowser.open_new(tweet_url)
