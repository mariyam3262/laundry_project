from django.urls import path

from home.views import index
from home.views import dashboard,OrderReport,CancelReport
app_name  = 'home'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home', dashboard, name='dashboard'),
    path('orders', OrderReport, name='report-order'),
    path('cancel_order', CancelReport, name='report-cancel')


]
