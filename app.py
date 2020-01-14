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
        count = request.form.get('count')

        content = twitter.search(query, count)

        # JSON file
        f = tempfile.NamedTemporaryFile(prefix='search_', suffix='.json', mode='w+', delete=False)
        print(f'JSON path: {f.name}')
        filename = os.path.basename(f.name)
        print(f'JSON filename: {filename}')
        json.dump(content, f)
        f.close()

        return redirect(url_for('search', filename=filename))
    return render_template('index.html', title='Twitter Search', form=form)

@app.route('/search/<filename>')
def search(filename):
    f = open(os.path.join(tempfile.gettempdir(), filename), "r")
    content = json.load(f)
    f.close()

    return render_template('search.html', title='Twitter Search', content=content, filename=filename)

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    print(f'Download JSON file: {filename}')
    return send_from_directory(tempfile.gettempdir(), filename, as_attachment=True)

if __name__ == '__main__':
    app.run()
