
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Client


class ClientCreateView():
    model = Client
    fields = ['first_name', 'last_name' , 'address','OIB']
    def get_success_url(self, **kwargs):
        return reverse('client-detail', args=[self.object.pk]) 