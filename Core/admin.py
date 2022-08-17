from http import client
from django.contrib import admin
from .models import Client, Service, Invoice, InvoiceService

admin.site.register((Client, Service, Invoice, InvoiceService))