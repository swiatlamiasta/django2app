from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('add_provider/', views.add_provider, name='add_provider'),
    path('providers/', views.providers, name='providers'),
    path('offers/', views.offers, name='offers'),
]
