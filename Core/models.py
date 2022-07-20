from django.db import models
#from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator


class Client(models.Model):
    first_name = models.CharField(max_length=16,  verbose_name="Ime")
    last_name = models.CharField(max_length=16, blank=True, verbose_name="Prezime")
    address = models.CharField(max_length=64,  blank=True, verbose_name="Adresa")
    #OIB = models.CharField(max_length=11, validators=[MinLengthValidator(11)], blank=True)
    OIB = models.IntegerField( blank=True, validators=[RegexValidator(regex='^.{11}$', message='Broj znamenki mora biti 11', code='nomatch')])

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Service(models.Model):
    service_name = models.CharField(max_length=64, verbose_name="Usluga")
    price = models.FloatField(verbose_name="Cijena")

    def __str__(self) -> str:
        return f'{self.service_name} {self.price}'



class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='invoices', verbose_name="Klijent")
    vat_percentage = models.PositiveSmallIntegerField(default=25,verbose_name="Porez")

    @property
    def total_price(self):
        return sum([service.service.price * service.quantity for service in self.invoice_services.all()])

    @property
    def total_price_inc_vat(self):
        return self.total_price + ((self.total_price/100) * self.vat_percentage)