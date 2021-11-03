from django.forms import (
    Form,
    CharField,
    DateTimeField,
)


class NewPostForm(Form):

    title = CharField()
    content = CharField()


class VisitForm(Form):

    visitor = CharField()
    date_time = DateTimeField()
    reason = CharField()
