from django.urls import path
from . import views

app_name = 'app02'

urlpatterns = [
    path('templates/', views.re, name='re'),
]
