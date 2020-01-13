from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Query', [
        DataRequired()
    ])
    count = IntegerField('Number of tweets per page', [
        DataRequired()
    ])
    submit = SubmitField('Submit')
