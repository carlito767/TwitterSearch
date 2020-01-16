from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from forms import SearchForm
import json
import os
import tempfile
import twitter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

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

        result = twitter.search(query, int(n), result_type, geocode)

        # JSON file
        f = tempfile.NamedTemporaryFile(prefix='search_', suffix='.json', mode='w+', delete=False)
        print(f'JSON path: {f.name}')
        filename = os.path.basename(f.name)
        print(f'JSON filename: {filename}')
        json.dump(result, f)
        f.close()

        search_id, extension = os.path.splitext(filename)
        print(f'Search ID: {search_id}')

        return redirect(url_for('search', search_id=search_id))
    return render_template('index.html', title='Twitter Search', form=form)

@app.route('/search/<search_id>')
def search(search_id):
    filename = search_id + '.json'
    f = open(os.path.join(tempfile.gettempdir(), filename), 'r')
    result = json.load(f)
    f.close()

    return render_template('search.html', title='Twitter Search', result=result, search_id=search_id)

@app.route('/download/<search_id>', methods=['GET', 'POST'])
def download(search_id):
    filename = search_id + '.json'
    print(f'Download JSON file: {filename}')
    return send_from_directory(tempfile.gettempdir(), filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
