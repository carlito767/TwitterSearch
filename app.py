from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    """Landing page."""
    return render_template('/index.html', title='Lame Site')

if __name__ == '__main__':
    app.run()
