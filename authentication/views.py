from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hooks import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.http import HttpResponseRedirect

def home(request):
    return render(request, "authentication/index.html")


def signup(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmed_password = request.POST['confirmed_password']
        
        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exists! Please try some other username.")
            print("s")
            return redirect('authentication:home')

        if User.objects.filter(email=email):
            messages.error(
                request, "Email is already registered!")
            print("d")
            return redirect('authentication:home')

        if len(username) > 20:
            messages.error(
                request, "Username must under 10 characters.")
            print("f")
            return redirect('authentication:home')

        if password != confirmed_password:
            messages.error(
                request, "Passwords didn't match!")
            print("ff")
            return redirect('authentication:home')
            return redirect('authentication:home')
        user = User.objects.create_user(username, email, password)
        user.first_name = name
        user.is_active = False
        user.save()
      
        # Welcome Email
        subject = 'Welcome to Hooks&Hangers - Admin'
        message = "Hello " + user.first_name + "! \n" + \
            "Welcome to Hooks&hangers! \n" + "Thank you for signing up \n" + \
            "We've also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking you\n Team Hooks&Hangers"
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confimation Email
        current_site = get_current_site(request)
        print(current_site)
        confirmation_subject = 'Confirm your email - Hooks&Hangers Admin Login!!'
        confirmation_message = render_to_string('email_confirmation.html', {
            'name': user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
        })
        email = EmailMessage(
            confirmation_subject,
            confirmation_message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        email.fail_silently = True
        email.send()

        return redirect('authentication:signin')

    return render(request, "authentication/signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.first_name
            return redirect('home:dashboard')
        else:
             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    return redirect('authentication:signin')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home:dashboard')
    else:
        return render(request, 'activation_failed.html')
