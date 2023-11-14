from .views import *
from django.urls import path


menuAppUrl = [
    path('', index, name='index'),
    path('about', about_view, name='about_view'),
]