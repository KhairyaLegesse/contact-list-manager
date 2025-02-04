from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField  
from wtforms.validators import DataRequired , Regexp , ValidationError #imported the data required

class ContactForm(FlaskForm):
    name = StringField('Name',
                       #this line will make sure the name is updated and not empty
                       validators=[DataRequired(message='Name is required'),
                                   #regex added to name so its only letters and not number
                                      Regexp(r'^[a-zA-Z ]*$', message="Name must be letters only")]) #validator added for name, also imported the validator
    #validator added to ensure it's not empty.
    phone = StringField('Phone', validators=[DataRequired(message="Phone number is required")])
# Custom phone number validator function to add additional checks for phone format.
    def validate_phone(form, field):
    # Get the value entered in the phone field.
        phone_number = field.data
    # Check if the phone number contains only digits.
        if not phone_number.isdigit():
        # If the phone number has non-numeric characters, raise a validation error.
          raise ValidationError("Phone number must be numeric.")
    # Check if the phone number length is exactly 8 digits.
        if len(phone_number) != 8:
        # If the phone number length is not 8, raise a validation error.
         raise ValidationError("Phone number must be exactly 8 digits.")
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 