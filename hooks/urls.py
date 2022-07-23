"""hooks_and_hangers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hooksadmin/',include('home.urls',namespace='home')),
    path('hooksadmin/customer/',include('customer.urls',namespace='customer')),
    path('hooksadmin/order/',include('order.urls',namespace='order')),
    path('hooksadmin/invoice/',include('invoice.urls',namespace='invoice')),
    path('hooksadmin/mbsp/',include('membership.urls',namespace='membership')),
    path('hooksadmin/user/',include('user.urls',namespace='user')),
    path('hooksadmin/notifications/',include('notifications.urls',namespace='noti')),
    path('hooksadmin/cust_barcode/',include('cust_barcode.urls',namespace='cust_barcode')),
    path('hooksadmin/expense/',include('expense.urls',namespace='expense')),
    path('hooksadmin/auth/',include('authentication.urls',namespace='authentication')),
    
    # path('workshop/',include('workshop.urls',namespace='workshop')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)