
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView , UpdateView
from django.shortcuts import redirect, render

from .models import Client, Service


def home(request):
    return redirect("invoice-list")  

class ClientCreateView(CreateView):

    model = Client
    fields = ['first_name', 'last_name' , 'address','OIB']
    def get_success_url(self, **kwargs):
        return reverse('client-detail', args=[self.object.pk]) 



class ServiceCreateView(CreateView):
    model = Service
    fields = ['service_name','price']
    def get_success_url(self, **kwargs):
        return reverse('service-detail', args=[self.object.pk]) 


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['first_name', 'last_name' , 'address','OIB']
    def get_success_url(self, **kwargs):
        return reverse('client-detail', args=[self.object.pk]) 


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['service_name', 'price']
    def get_success_url(self, **kwargs):
        return reverse('service-detail', args=[self.object.pk]) 

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['first_name', 'last_name' , 'address','OIB']
    def get_success_url(self, **kwargs):
        return reverse('client-detail', args=[self.object.pk]) 


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['service_name', 'price']
    def get_success_url(self, **kwargs):
        return reverse('service-detail', args=[self.object.pk]) 