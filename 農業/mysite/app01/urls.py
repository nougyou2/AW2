from django.urls import path
from . import views

app_name = 'app01'

urlpatterns = [
    path('templates/', views.top, name='top'),
]
