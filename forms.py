from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL

class AddCafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    map_url = StringField("Map", validators=[DataRequired(), URL()])
    img_url = StringField("Image", validators=[DataRequired(), URL()])
    location = StringField("City", validators=[DataRequired()])
    seats = StringField("Seats", validators=[DataRequired()])
    has_toilet = BooleanField("Toilet", validators=[DataRequired()])
    has_wifi = BooleanField("Wifi", validators=[DataRequired()])
    has_sockets = BooleanField("Sockets", validators=[DataRequired()])
    can_take_calls = BooleanField("Calls", validators=[DataRequired()])
    coffee_price = StringField("Prices", validators=[DataRequired()])
    submit = SubmitField("Submit Post")