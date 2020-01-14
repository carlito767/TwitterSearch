from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()], render_kw={'autofocus': True})
    count = IntegerField('Number of tweets per page', validators=[DataRequired()], default=1)
    submit = SubmitField('Submit')

class ResultsForm(FlaskForm):
    download = SubmitField('Download JSON')
