from django.db import models
from django.utils import timezone

class company_info(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    postnr = models.IntegerField()
    by = models.CharField(max_length=40)
    tlf = models.CharField(max_length=40)
    email = models.EmailField()
    bank = models.CharField(max_length=40)
    regnr = models.CharField(max_length=40)
    kontonr = models.CharField(max_length=40)
