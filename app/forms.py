from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Optional

class SearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired(), Length(min=3)], render_kw={'autofocus': True})
    no_retweets = BooleanField('No Retweets', default=True)
    n = IntegerField('Number of tweets', validators=[DataRequired()], default=15)
    language = StringField('Language')
    result_type = SelectField('Type of results', choices=[('mixed', 'Mixed'), ('recent', 'Recent'), ('popular', 'Popular')], default='recent')
    since = DateField('Since', validators=[Optional()])
    until = DateField('Until', validators=[Optional()])
    geocode = StringField('Geocode')
    submit = SubmitField('Submit')
