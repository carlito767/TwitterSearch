from flask import Flask

app = Flask(__name__)
# Remove empty lines in Jinja2 generated output
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

from app import views
