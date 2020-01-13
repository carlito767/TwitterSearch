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
    count = request.form.get('count')

    content = twitter.search(query, count)

    return render_template('search.html', title='Twitter Search', content=content)

    # return Response(json.dumps(content), 
    #     mimetype='application/json',
    #     headers={'Content-Disposition':'attachment;filename=search.json'})

if __name__ == '__main__':
    app.run()
