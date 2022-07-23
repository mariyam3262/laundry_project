
from multiprocessing import AuthenticationError
from django.contrib import messages
from telnetlib import AUTHENTICATION
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth


from .models import User


def indexView(request):
    if request.method == 'GET':
        return render(request,'user/index.html')

# @login_required()


def LoginView(request):
    if request.method == 'GET':
        return render(request,'user/login.html')

    if request.method == 'POST':
        detail=request.POST
        print(detail)
        users = User.objects.all()
        print(users)
        for user in users:
            if user.username == detail['uname'] and user.password == detail['pass']:  
                print(user)      
                return render(request,'user/dashboard.html')


def LogoutView(request):

    if request.method == 'GET':
        return render(request,'user/login.html')

def dashboardView(request):
    user = {
        'username':request.POST['uname']
    }
    return render(request,'user/dashboard.html',{'user'})

def registerView(request):

    if request.method =='GET':
        return render(request,'user/register.html')


    if request.method == 'POST':
        detail=request.POST
        print(detail)
        user=User()
        user.username=detail['uname']
        user.password=detail['pass']        
        user.password_confirm=detail['c_pass']
        user.m_number=detail['mnum']
        user.email= detail['email']
        if len(detail['pass']) > 6 and len(detail['pass']) < 12:
            if  detail['pass'] == detail['c_pass']:
                if User.objects.filter(email=detail['email']).exists():
                    messages.success(request,f'Email Taken')
                    return render(request,'user/register.html')
                elif User.objects.filter(username=detail['uname']).exists():
                    messages.success(request,f'Username Taken')
                    return render(request,'user/register.html')
                else:    
                    user.save()
                    print('user created')
                    return render(request,'user/index.html')
            else:
                messages.success(request,f"Password don't match!")
                return render(request,'user/register.html')
        else:
            messages.success(request,f"password length mismatch")
            return render(request,'user/register.html')
    

