from django.forms import (
    Form,
    CharField,
)


class UserForm(Form):

    user = CharField()
    email = CharField()
