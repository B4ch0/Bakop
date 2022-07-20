from django.contrib import admin

from .models import Client, Service, Invoice

admin.site.register((Client, Service, Invoice))