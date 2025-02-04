from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField , validators #imported the validators
from wtforms.validators import DataRequired , Regexp#imported the data required

class ContactForm(FlaskForm):
    name = StringField('Name',
                       #this line will make sure the name is updated and not empty
                       validators=[DataRequired(message='Name is required'),
                                   #regex added to name so its only letters and not number
                                      Regexp(r'^[a-zA-Z ]*$', message="Name must be letters only")]) #validator added for name, also imported the validator
    phone = StringField('Phone')
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 