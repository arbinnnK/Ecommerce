from django.shortcuts import render, HttpResponse
from products.models import Product
from contents.models import Content

def show_home(request):
    products = Product.objects.order_by('-id')[:2]
    sliders = Content.objects.filter(section__title='Slider')
    # return HttpResponse(sliders)
    return render(request, 'index.html', {'sliders': sliders, 'latest': products})

def show_content(request, section):
    
    data = Content.objects.filter(section__title=section)
    return render(request, 'content.html', {'data': data})

def show_about(request):
    section = ''
    data = Content.objects.filter(section__title=section)
    return HttpResponse('About us')

def show_contacts(request):
    section = ''
    data = Content.objects.filter(section__title=section)
    return HttpResponse('Contact us')

def show_policies(request):
    section = ''
    data = Content.objects.filter(section__title=section)
    return HttpResponse('Policies')

# Create your views here.
