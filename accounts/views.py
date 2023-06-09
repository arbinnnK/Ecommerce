from django.shortcuts import render, HttpResponse, redirect
from accounts.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password


def login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']

        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials')
            return redirect('home')
          

   



def register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        mb = request.POST['mb']
        ad = request.POST['ad']
        un = request.POST['un']
        pw = make_password(request.POST['pw'])
        

        user = User(first_name=fn, last_name=ln, email=em, mobile=mb, address=ad, username=un, password=pw)
        user.save()
        return redirect('home')
        
    
    return HttpResponse('Invalid Access')



def logout(request):
    auth.logout(request)
    messages.warning(request, 'You are logged out!')
    return redirect('home')

def update_profile(request):
    pass

def change_password(request):
    pass