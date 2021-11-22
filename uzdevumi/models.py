from django.db import models

# kolonnu nosaukumi, ja izmaina tad db tabula noklāsies :)
class Visit(models.Model):
    visitor = models.CharField(max_length=100)
    reason = models.CharField(max_length=140)
    date_time = models.DateTimeField()
