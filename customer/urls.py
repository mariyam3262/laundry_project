from django.contrib import admin
from django.urls import path

from customer.views import ActiveCustomer, CustomerListView,CustomerCreateView,CustomerDetailView,CustomerDeleteView,CustomerUpdateView,UnactiveCustomer
app_name  = 'customer'
urlpatterns = [
    path('list/',CustomerListView,name='list'),
    path('create/',CustomerCreateView,name='create'),
    path('<int:pk>/detail/',CustomerDetailView,name='details'),
    path('<int:pk>/delete/',CustomerDeleteView,name='delete'),
    path('<int:pk>/update/',CustomerUpdateView,name='update'),
    path('active_customer/',ActiveCustomer,name='active_customer'),
    path('inactive_customer/',UnactiveCustomer,name='inactive_customer')

]
