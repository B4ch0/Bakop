
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    
    path('klijenti/', name='client-list'),

    path('klijent/novi/' , name='client-new'),