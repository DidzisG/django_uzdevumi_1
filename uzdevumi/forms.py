from django.forms import (
    Form,
    CharField,
    DateTimeField,
)


class VisitForm(Form):

    visitor = CharField()
    email = CharField()
