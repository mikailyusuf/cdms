from django.shortcuts import render
from .models import Customers

# Create your views here.

def home(request):
    customers = Customers.objects.all()
    context = {'customers':customers }
    return render(request,'customers/dashboard.html',context)
