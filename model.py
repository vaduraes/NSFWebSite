from wtforms import Form, FloatField, validators

class InputForm(Form):
    A_Lat = FloatField(
        label='Departure Latitude', default=34.17283435158192,
        validators=[validators.InputRequired()])
    A_Long = FloatField(
        label='Departure Longitude', default=-77.94775642333315,
        validators=[validators.InputRequired()])
    B_Lat = FloatField(
        label='Destination Latitude', default=34.24566333445864,
        validators=[validators.InputRequired()])
    B_Long = FloatField(
        label='Destination Longitude', default=-77.87258546124485,
        validators=[validators.InputRequired()])