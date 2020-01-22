# Sources:
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
# https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators
# http://benalexkeen.com/interacting-with-the-twitter-api-using-python/
# https://stackoverflow.com/questions/38717816/twitter-api-text-field-value-is-truncated
# https://preslav.me/2019/01/09/dotenv-files-python/

import base64
import json
import os
import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

def get_bearer_token(consumer_key, consumer_secret):
    key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    bearer_token = auth_resp.json()['access_token']
    return bearer_token

def search(bearer_token, query, n, result_type, geocode):
    print(f'Query: {query}')
    print(f'Number of tweets: {n}')
    print(f'Type of results: {result_type}')
    print(f'Geocode: {geocode}')

    result = { 'tweets':[] }
    max_tweets_per_request = 100
    max_id = None
    while n > 0:
        count = min(n, max_tweets_per_request)
        n -= count

        search_headers = {
            'Authorization': 'Bearer {}'.format(bearer_token)
        }
        search_params = {
            'q': query,
            'count': count,
            'result_type': result_type,
            'geocode': geocode,
            'max_id': max_id,
            'tweet_mode': 'extended'
        }
        search_url = '{}1.1/search/tweets.json'.format(base_url)
        try:
            search_resp = requests.get(search_url, headers=search_headers, params=search_params)
            search_resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f'Error: {err}')
        else:
            content = json.loads(search_resp.content)
            for tweet in content['statuses']:
                id = tweet['id']
                if max_id is None or max_id > id:
                    max_id = id
                result['tweets'].append(tweet)

    return result
