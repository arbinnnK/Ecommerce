from django.shortcuts import render, redirect
from django.contrib import messages
from shopping.models import *

def add_to_wishlist(request, pid):
    wl = Wishlist.objects.filter(user=request.user).filter(product_id=pid)
    if not wl:
        wl = Wishlist(user_id=request.user.id, product_id=pid)
    
        wl.save()
        messages.info(request, 'Item added to you Wishlist!')

    else:
        messages.info(request, 'Item already exist!')
    return redirect('home')


def remove_from_wishlist(request):
    pass

def add_to_cart(request, pid, qty):
    cart = Cart.objects.filter(user=request.user).filter(product_id=pid)
    if not cart:
        cart = Wishlist(user_id=request.user.id, product_id=pid)
    
        cart.save()
        messages.info(request, 'Item added to your cart!')

    else:
        messages.info(request, 'Item already exist!')
    return redirect('home')


def remove_from_cart(request):
    pass

def checkout(request):
    pass

def comment(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        cmt = request.POST['comment']

        comment = Comment(user=request.user, product_id=pid, comment=cmt)
        comment.save()
        return redirect('home')
        

def review(request):
    pass

def show_wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist})

def show_cart(request):
    pass

def checkout(request):
    pass