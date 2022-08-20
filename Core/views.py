
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView
from django.shortcuts import redirect, render

from .models import Client, InvoiceService, Service, Invoice


def home(request):
    return redirect("invoice-list")  


class ClientListView(ListView):
    paginate_by = 20
    model = Client


class ServiceListView(ListView):
    paginate_by = 20
    model = Service
    ordering = ['-pk']


class InvoiceListView(ListView):
    paginate_by = 20
    model = Invoice

class ClientDetailView(DetailView):
    model = Client


class ServiceDetailView(DetailView):
    model = Service


class InvoiceDetailView(DetailView):
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

class InvoiceUpdateView(UpdateView):
    model = Invoice
    fields = ['client','vat_percentage']

    def get_success_url(self, **kwargs):
        return reverse('invoice-detail', args=[self.object.pk]) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["invoice_services"] = InvoiceService.objects.filter(invoice=self.get_object()).all()
        context["service_values"] = { service.service.service_name : service.quantity for service in context["invoice_services"]}
        return context
    
    def post(self, request, **kwargs):
        self.object = self.get_object()
        service_post = {k.replace('num_',''):v for (k,v) in request.POST.items() if 'num_' in k}
        for invoice_service in self.object.invoice_services.all():
            if invoice_service.service.service_name in service_post and service_post[invoice_service.service.service_name]!='0' and service_post[invoice_service.service.service_name]!='':
                invoice_service.quantity = int(service_post[invoice_service.service.service_name])
                invoice_service.save()
            elif invoice_service.service.service_name in service_post and (service_post[invoice_service.service.service_name]=='0' or service_post[invoice_service.service.service_name]==''):
                invoice_service.delete()
            service_post.pop(invoice_service.service.service_name)
        for k,v in service_post.items():
            service = Service.objects.get(service_name=k.replace('num_',''))
            if v !='':
                InvoiceService.objects.create(service= service,invoice= self.object, quantity=int(v))
        self.object.save()
        return super(InvoiceUpdateView, self).post(request, **kwargs)

