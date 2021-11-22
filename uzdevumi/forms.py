from django.forms import (
    Form,
    CharField,
)


class VisitForm(Form):

    user = CharField()
    email = CharField()
