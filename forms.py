from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()], render_kw={'autofocus': True})
    no_retweets = BooleanField('No Retweets', default=True)
    n = IntegerField('Number of tweets', validators=[DataRequired()], default=15)
    geocode = StringField('Geocode')
    submit = SubmitField('Submit')
