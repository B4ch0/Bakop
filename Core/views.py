
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView , UpdateView
from django.shortcuts import redirect, render

from .models import Client, Service, Invoice


def home(request):
    return redirect("invoice-list")  

class ClientListView(ListView):
    model = Client


class ServiceListView(ListView):
    model = Service
   

class InvoiceListView(ListView):
    model = Invoice


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

class InvoiceCreateView(CreateView):
    model = Invoice
    fields = ['client','vat_percentage']

    def get_success_url(self, **kwargs):
        return reverse('invoice-detail', args=[self.object.pk]) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save()
        for (k,v) in form.data.items():
            if k.startswith('num_') and len(v) > 0 and v != '0' :
                service = Service.objects.get(service_name=k.replace('num_',''))
                InvoiceService.objects.create(service= service,invoice= self.object, quantity=int(v))
        return HttpResponseRedirect(self.get_success_url())