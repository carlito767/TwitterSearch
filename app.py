from flask import Flask, redirect, render_template, request, url_for
from forms import SearchForm

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
    return f'Request : {query}'

if __name__ == '__main__':
    app.run()
