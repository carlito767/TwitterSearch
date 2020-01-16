from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()], render_kw={'autofocus': True})
    no_retweets = BooleanField('No Retweets', default=True)
    n = IntegerField('Number of tweets', validators=[DataRequired()], default=15)
    result_type = SelectField('Type of results', choices=[('mixed', 'Mixed'), ('recent', 'Recent'), ('popular', 'Popular')], default='recent')
    geocode = StringField('Geocode')
    submit = SubmitField('Submit')
