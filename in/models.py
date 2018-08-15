from django.db import models
from django.utils import timezone

class CompanyInfo(models.Model):
    name = models.CharField(max_length=70)
    address = models.TextField()
    postnr = models.IntegerField()
    by = models.CharField(max_length=15)
    tlf = models.CharField(max_length=15)
    email = models.EmailField()
    bank = models.CharField(max_length=50)
    regnr = models.IntegerField()
    kontonr = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
