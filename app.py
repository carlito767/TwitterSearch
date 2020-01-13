from flask import Flask, redirect, render_template, request, Response, url_for
from forms import SearchForm
import json
import twitter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search'))
    return render_template('index.html', title='Twitter Search', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    content = twitter.search(query)
    tweet_id = content['statuses'][0]['id']
    tweet_url = f'https://twitter.com/user/status/{tweet_id}'
    # return f'Request: {query}, tweet url: <a href="{tweet_url}">{tweet_url}</a>'

    return Response(json.dumps(content), 
        mimetype='application/json',
        headers={'Content-Disposition':'attachment;filename=search.json'})

if __name__ == '__main__':
    app.run()
