# Sources:
# https://blog.goodaudience.com/using-the-twitter-api-with-python-c6e8da96d273
# https://preslav.me/2019/01/09/dotenv-files-python/

import base64
import json
import os
import requests

# Settings
from dotenv import load_dotenv
load_dotenv()

# Consumer API keys
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

__key_ascii = '{}:{}'.format(API_KEY, API_SECRET_KEY).encode('ascii')
__key_base64 = base64.b64encode(__key_ascii)
__key_base64 = __key_base64.decode('ascii')

__base_url = 'https://api.twitter.com/'

def __authenticate():
    auth_headers = {
        'Authorization': 'Basic {}'.format(__key_base64),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_url = '{}oauth2/token'.format(__base_url)
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    print(f'Authentication status: {auth_resp.status_code}')
    access_token = auth_resp.json()['access_token']
    return access_token

def search(query):
    print(f'Query: {query}')

    # Authentication
    access_token = __authenticate()

    # Search
    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    search_params = {
        'q': query,
        'result_type': 'recent',
        'count': 1
    }
    search_url = '{}1.1/search/tweets.json'.format(__base_url)
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    print(f'Search status: {search_resp.status_code}')

    content = json.loads(search_resp.content)
    return content
