
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (home, 
    ClientListView, ServiceListView, 
    ClientDetailView , ServiceDetailView,
    ClientCreateView , ServiceCreateView,
    ClientUpdateView , ServiceUpdateView,
    )

urlpatterns = [
    path("", home, name="home"),
    
    path('klijenti/', login_required(ClientListView.as_view(template_name='Core/client-list.html')), name='client-list'),
    path('usluge/', login_required(ServiceListView.as_view(template_name='Core/service-list.html')), name='service-list'),
    path('racuni/', login_required(InvoiceListView.as_view(template_name='Core/invoice-list.html')), name='invoice-list'),


   

    path('klijent/<int:pk>/', login_required(ClientDetailView.as_view(
        template_name='Core/client-detail.html')), name='client-detail'),
    path('usluga/<int:pk>/', login_required(ServiceDetailView.as_view(
        template_name='Core/service-detail.html')), name='service-detail'),
            path('racun/<int:pk>/', login_required(InvoiceDetailView.as_view(
        template_name='Core/invoice-detail.html')), name='invoice-detail'),
   

     path('klijent/izmjena/<int:pk>/', login_required(ClientUpdateView.as_view(
        template_name='Core/client-update.html')), name='client-update'),
    path('usluga/izmjena/<int:pk>/', login_required(ServiceUpdateView.as_view(
        template_name='Core/service-update.html')), name='service-update'),
   
   
   
    path('klijent/novi/', login_required(ClientCreateView.as_view(
        template_name='Core/client-new.html')), name='client-new'),
    path('usluga/nova/', login_required(ServiceCreateView.as_view(
        template_name='Core/service-new.html')), name='service-new'),
    path('racun/novi/', login_required(InvoiceCreateView.as_view(
        template_name='Core/invoice-new.html')), name='invoice-new'),
    