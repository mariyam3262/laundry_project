from django.contrib import admin
from django.urls import path

from user.views import  indexView,dashboardView,registerView,LogoutView,LoginView


app_name='user'
urlpatterns = [
    path('home/',indexView,name="home"),
    path('dashboard/',dashboardView,name="dashboard"),
    path('register/',registerView,name="register"),
    path('login/',LoginView,name="login"),
    path('logout/',LogoutView,name="logout"),
    


]

