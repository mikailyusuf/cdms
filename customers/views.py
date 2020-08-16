from django.shortcuts import render
from .models import Customers

# Create your views here.


def customers(request):
    customers = Customers.objects.all()
    context = {'customers':customers }
    return render(request,'customers/customers.html',context)


def customer(request, pk):
    customer = Customers.objects.get(id=pk)
    context = {'customer': customer}
    return render(request, 'customers/customer.html', context)

def dashboard(request):

    return render(request,'customers/dashboard.html')