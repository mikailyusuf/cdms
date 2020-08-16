from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('', views.dashboard, name='dashboard'),

]