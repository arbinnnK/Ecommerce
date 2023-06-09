from django.shortcuts import render, HttpResponse
from products.models import Product

def show_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
# django query system 

def show_products_details(request, id):
    products = Product.objects.filter(id=id)
    product = Product.objects.get(id=id)
    return HttpResponse(products[0].price)
# Create your views here.
