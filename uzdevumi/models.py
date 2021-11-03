from django.db import models


class Visit:

    def __init__(self, visitor, date_time, reason):

        self.visitor = visitor
        self.date_time = date_time
        self.reason = reason
