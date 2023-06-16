from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()
    order_count = Order.objects.count()
    pending_orders = Order.objects.filter(status='Pending').count()
    delivered_orders = Order.objects.filter(status='Delivered').count()

    context = {'orders': order,'order_count':order_count,'pending_orders':pending_orders,'delivered_orders':delivered_orders, 'customers':customer}
    return render(request,"accounts/dashboard.html",context)

def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = customer.order_set.all().count()

    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders}
    return render(request,"accounts/customers.html",context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,"accounts/products.html",context)

