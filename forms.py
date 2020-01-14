from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()], render_kw={'autofocus': True})
    no_retweets = BooleanField('No Retweets', default=True)
    count = IntegerField('Number of tweets per page', validators=[DataRequired()], default=1)
    submit = SubmitField('Submit')
