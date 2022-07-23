from django.urls import path
from .views import BarcodeList,OrderBarcode


app_name = 'cust_barcode'
urlpatterns = [

    path('list/', BarcodeList, name="list"),
    path('order_barcode/<int:pk>/', OrderBarcode, name="order_barcode"),
    

]