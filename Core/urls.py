
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    
    path('klijenti/', name='client-list'),
    path('usluge/', name='service-list'),
    path('usluga/nova/', name='service-new'),
    path('klijent/novi/' , name='client-new'),
    path('klijent/<int:pk>/', name='client-detail'),
    path('usluga/<int:pk>/', name='service-detail'),