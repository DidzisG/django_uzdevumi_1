from django.db import models

# kolonnu nosaukumi, ja izmaina tad db tabula noklāsies :)
class User(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=140)
