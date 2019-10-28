from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('templates/', views.index, name='index'),
]