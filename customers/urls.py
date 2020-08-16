from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('', views.dashboard, name='dashboard'),
    path('add_customer',views.addCustomer, name =  'addCustomer'),
    path('update_customer/<str:pk>/', views.updateCustomer, name='updateCustomer'),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name='deleteCustomer'),
]