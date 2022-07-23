from django.urls import path
from order.views import AddOrderToCart, AddToCart,ClearCart, EmailInvoice, InvoiceDetail,OrderList,OrderDetail,CancelOrder,OrderUpdate,AddPrice,SaveOrder,DeleteCart, UpdateCart,UpdatePayment, WorkshopList, AddCustomerOrder, AddToOrder2,AddType,AddClothType
app_name  = 'order'
urlpatterns = [
   

    path('addtocart/', AddToCart, name='addtocart'),
    path('empty-list/', ClearCart, name='emptylist'),
    path('list/', OrderList, name='list'),
    path('<int:pk>/detail/', OrderDetail, name='detail'),
    path('<int:pk>/invoice_detail/', InvoiceDetail, name='invoice_detail'),
    path('<int:pk>/email_invoice/', EmailInvoice, name='email_invoice'),
    path('<int:pk>/cancle/', CancelOrder, name='cancle'),
    path('<int:pk>/update/', OrderUpdate, name='update'),
    path('add_price/', AddPrice, name='add_price'),
    path('add_type/', AddType, name='add_type'),
    path('add_cloth_type/', AddClothType, name='add_cloth_type'),
    # path('save_order/', SaveOrder, name='save_order'),
    path('save_order/<int:customer_id>/', SaveOrder, name='save_order'),
    path('delete_cart/<int:pk>', DeleteCart, name='delete_cart'),
    path('payment_update/<int:pk>', UpdatePayment, name='payment_update'),
    path('workshop_list/', WorkshopList, name='workshop_list'),
    path('add_order_customer/', AddCustomerOrder, name='add_order_customer'),
    path('add_order_two/', AddToOrder2, name='add_order_two'),
    path('add_order_to_cart/<int:customer_id>/', AddOrderToCart, name='add_order_to_cart'),
    path('update_cart/', UpdateCart, name='update_cart'),

]
    
