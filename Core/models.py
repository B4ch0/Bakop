from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=16,  verbose_name="Ime")
    last_name = models.CharField(max_length=16, null=True, blank=True, verbose_name="Prezime")
    address = models.CharField(max_length=64, null=True, blank=True, verbose_name="Adresa")
    OIB = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Service(models.Model):
    service_name = models.CharField(max_length=64, verbose_name="Usluga")
    price = models.FloatField(verbose_name="Cijena")

    def __str__(self) -> str:
        return f'{self.service_name} {self.price}'