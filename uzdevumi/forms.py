from django.forms import (
    Form,
    CharField,
    FileField,
    Field
)


class UserForm(Form):

    user = CharField()
    email = CharField()

