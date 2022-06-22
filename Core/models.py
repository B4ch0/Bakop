from django.db import models


class Klijent(models.Model):
    ime = models.CharField(max_length=16, null=True)
   

