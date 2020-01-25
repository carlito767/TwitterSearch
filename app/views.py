from app import app, twitter
from app.forms import SearchForm
from flask import redirect, render_template, request, send_from_directory, url_for
import json
import os
import re
import tempfile
import time

# Bearer token
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
BEARER_TOKEN = twitter.get_bearer_token(API_KEY, API_SECRET_KEY)

# Template filters
@app.template_filter()
def tweet_datetime(datetime, format='%a %b %d %Y %H:%M:%S'):
    return time.strftime(format, time.strptime(datetime,'%a %b %d %H:%M:%S +0000 %Y'))

@app.template_filter()
def tweet_links(text):
    # Twitter link
    r = re.sub(r'(https://t.co/[\d\w\.]+)', r'<a href="\1" class="tweet-link">\1</a>', text)
    # Hashtag
    r = re.sub(r'#([\d\w\.]+)', r'<a href="https://twitter.com/hashtag/\1" class="tweet-hashtag">#\1</a>', r)
    # Twitter user
    r = re.sub(r'@([\d\w\.]+)', r'<a href="https://twitter.com/\1" class="tweet-user">@\1</a>', r)
    # Tweet text with links
    return r

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        query = request.form.get('query')
        no_retweets = request.form.get('no_retweets')
        n = request.form.get('n')
        result_type = request.form.get('result_type')
        since = request.form.get('since')
        until = request.form.get('until')
        geocode = request.form.get('geocode')

        if no_retweets:
            query += ' -filter:retweets'

        if since:
            query += f' since:{since}'

        if until:
            query += f' until:{until}'

        result = twitter.search(BEARER_TOKEN, query, int(n), result_type, geocode)

        # JSON file
        f = tempfile.NamedTemporaryFile(prefix='search_', suffix='.json', mode='w+', encoding='utf-8', delete=False)
        print(f'JSON path: {f.name}')
        filename = os.path.basename(f.name)
        print(f'JSON filename: {filename}')
        json.dump(result, f, ensure_ascii=False)
        f.close()

        search_id, extension = os.path.splitext(filename)
        print(f'Search ID: {search_id}')

        return redirect(url_for('search', search_id=search_id))
    return render_template('index.html', title='Twitter Search', form=form)

@app.route('/search/<search_id>')
def search(search_id):
    filename = search_id + '.json'
    f = open(os.path.join(tempfile.gettempdir(), filename), mode='r', encoding='utf-8')
    result = json.load(f)
    f.close()

    return render_template('search.html', title='Twitter Search', tweets=result['tweets'], search_id=search_id)

@app.route('/download/<search_id>', methods=['GET', 'POST'])
def download(search_id):
    filename = search_id + '.json'
    print(f'Download JSON file: {filename}')
    return send_from_directory(tempfile.gettempdir(), filename, as_attachment=True)
