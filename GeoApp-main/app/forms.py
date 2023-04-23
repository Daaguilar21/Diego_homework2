from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CapitalSearchForm(FlaskForm):
    ISO = StringField('Enter ISO3166 Country ID', validators=[DataRequired()])
    submit = SubmitField('Search')

class CountrySearchForm(FlaskForm):
    country_name = StringField('Country Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class CitySearchForm(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class CurrencyFilterForm(FlaskForm):
    currency_code = StringField('Currency Code', validators=[DataRequired()])
    submit = SubmitField('Filter')