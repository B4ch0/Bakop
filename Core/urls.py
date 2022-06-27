
from django.urls import path

urlpatterns = [
    path("", home, name="home"),

    path('klijent/novi/' , name='client-new'),