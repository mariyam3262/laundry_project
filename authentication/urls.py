from django.urls import path
from . import views
app_name='authentication'

urlpatterns = [
    path('home', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('activate,<uidb64>/<token>', views.activate, name="activate"),
]
