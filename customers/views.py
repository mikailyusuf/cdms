from django.shortcuts import render,redirect
from .models import Customers
from .forms import CustomerForm

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


def addCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'customers/add_customer.html', context)


def updateCustomer(request,pk):
    customer = Customers.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'customers/add_customer.html', context)


def deleteCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {'customer':customer}
    return render(request,'customers/delete_customer.html', context)


