# TwitterSearch

Search for tweets using Twitter Standard API

# Getting started


* Get [your Twitter API tokens](https://developer.twitter.com/en/docs/basics/getting-started)

* Clone this repository:

```
git clone --recursive https://github.com/carlito767/TwitterSearch
```

* Install [Python](https://www.python.org/)
* Add __Python__ and __Python Scripts__ (containing `pip` executable) directories to PATH

* Install project dependencies (from project directory):

```
pip install -r requirements.txt
```

* Copy `.env.example` to `.env` and update environment variables:

```
# Consumer API keys
API_KEY=<your_twitter_consumer_api_key>
API_SECRET_KEY=<your_twitter_consumer_secret_api_key>
```

# How to run

* Launch the app:

```
flask run
```

* Open this URL in your browser: http://localhost:5000/
