from wtforms import Form, StringField, SelectField
class MusicSearchForm(Form):
    choices = [('Garment Layer', 'Artist'),
               ('Colour', 'Colour'),
               ('ID', 'ID')]
    select = SelectField('Search for garment:', choices=choices)
    search = StringField('')