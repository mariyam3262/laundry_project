from operator import inv
from django.urls import reverse

from django.shortcuts import render, redirect
from invoice.models import Invoice
from invoice.models import ItemPrice
from order.models import Order, Cart
from customer.models import Customer
from datetime import datetime,timedelta
from membership.models import CustomerMembership
from cust_barcode.models import Barcode
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from notifications.views import message_data
from datetime import date,timedelta
d=date.today()-timedelta(days=7)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
# from wkhtmltopdf.views import PDFTemplateResponse  
import json
from django.contrib.sites.shortcuts import get_current_site
from hooks.settings import BASE_DIR,EMAIL_HOST_USER
from django.core.mail import send_mail,EmailMessage
import os


def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)

    return obj

@login_required
def AddToOrder2(request):
    if request.method == 'POST':
        detail = request.POST
        no_item = 1
        cart = Cart()
        cart.cust_id_id = detail['customer_name']
        cart.cust_type = detail['type']
        cart.service  = detail['service']
        cart.product = detail['product']
        def item_price(type, service, product):
            itemprice = ItemPrice.objects.all()
            for i in itemprice:
                if i.cust_type == type and i.service == service and i.cloth_type == product:
                    return i.price
        price = item_price (detail['type'], detail['service'], detail['product'])            
        cart.ind_price = price
        cart.no_item = no_item + 0
        cart.total_price = int(price) * int(no_item)
        cart.remarks = "nkjb"
        cart.save()
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




@login_required
def AddType(request):
    itemprice = ItemPrice.objects.all()
    type =  set()
    if request.method == "POST":
        service  = request.POST['service']
        for i in itemprice:
            if i.service == service:
                type.add(i.cust_type)
        json_str = json.dumps(type, default=serialize_sets)
        return JsonResponse({"type": json_str}, status=200)
    else:
        return JsonResponse({"error": ""}, status=400)



@login_required
def AddClothType(request):
    print("cust_type")
    itemprice = ItemPrice.objects.all()
    product =  set()
    if request.method == "POST":
        service  = request.POST['services']
        cust_type  = request.POST['cust_type']
        for i in itemprice:
            if i.service == service and i.cust_type == cust_type:
                product.add(i.cloth_type)
        json_str = json.dumps(product, default=serialize_sets)
        return JsonResponse({"product": json_str}, status=200)
    else:
        return JsonResponse({"error": ""}, status=400)



@login_required
def AddCustomerOrder(request):
    customers = Customer.objects.all()
    return render(request,'order/add_order_customer.html',{'customers':customers})


@login_required
def AddOrderToCart(request, customer_id):
    customer_id = customer_id
    customers = Customer.objects.all()
    carts = Cart.objects.all()
    itemprice = ItemPrice.objects.all()
    cust_type = set()
    product = set()
    service = set()
    for item in itemprice:
        cust_type.add(item.cust_type)
        product.add(item.cloth_type)
        service.add(item.service)
    

    customer = Customer.objects.get(pk=customer_id)
    cart_data = Cart.objects.filter(cust_id_id=customer_id)
    total_peice = 0

    total_price = 0

    for cart_total in cart_data:
        total_peice = total_peice+cart_total.no_item
        total_price = total_price+cart_total.total_price
    datas = {
        'name': Customer.objects.get(pk = customer_id).customer_name,
        'no_item': total_peice,
        'total_price' : total_price,
        'date':datetime.now().date,
        'due_date': datetime.now()+timedelta(days=5)
    }
        # return render(request,'order/add_order_2.html',{'customer_id':int(customer_id),'cust_type':cust_type,'product':product,'service':service,'customers':customers,'carts':carts,'datas':datas})
    return render(request,'order/add_order_2.html',{'customer_id':int(customer_id),'cust_type':cust_type,'product':product,'service':service,'customers':customers,'carts':carts,'datas':datas})




@login_required
def UpdateCart(request):
    if request.method == "POST":
        cart_id  = request.POST['cart_id']
        quantity  = request.POST['quantity']
        cart = Cart.objects.get(pk=cart_id)
        carts = Cart.objects.filter(cust_id_id=cart.cust_id_id)
        total_peice = 0
        grand_total_price = 0
        for cart_total in carts:
            total_peice = total_peice+cart_total.no_item
            grand_total_price = grand_total_price+cart_total.total_price
        print(grand_total_price)
        cart.no_item = quantity
        cart.total_price = int(cart.ind_price) * int(quantity)
        cart.save()
        return JsonResponse({"total_price": cart.total_price,'grand_total_price':grand_total_price,'total_peice':total_peice}, status=200)
    else:
        return JsonResponse({"error": ""}, status=400)





@login_required
def SaveOrder(request,customer_id):
    carts = Cart.objects.filter(cust_id_id = customer_id).first()
    cart_as = Cart.objects.filter(cust_id_id = carts.cust_id_id).first()
    order = Order.objects.filter(cust_id_id = cart_as.cust_id_id).last()
    if request.method == 'POST':
        detail = request.POST
        data = {
        'date':datetime.now(),
        'due_date' : datetime.now()+timedelta(days=5),
        'net_price': detail['net_price'],
        'discount' : detail['discount'],
        'discount_type' : detail['discount_type'],
        'payment_due' : detail['payment_due']
        
        }
        cart = Cart.objects.filter(cust_id_id = customer_id).first()
        ocart = Cart.objects.filter(cust_id_id = customer_id)              
        invoice = Invoice()
        invoice.cust_id_id = cart.cust_id_id
        for item in ocart:
            invoice.total_piece = invoice.total_piece + item.no_item
            invoice.price = invoice.price + item.ind_price
            invoice.net = invoice.net + item.total_price

        invoice.date = datetime.now()
        invoice.due_date = datetime.now()+timedelta(days=5)
        invoice.discount = detail['discount']
        invoice.payment_due = detail['payment_due']
        invoice.discount_type =  detail['discount_type']
        cmbsp = CustomerMembership.objects.all()
        for cm in cmbsp:
            if cm.custid_id == cart.cust_id_id:
                invoice.m_point = CustomerMembership.objects.get(custid_id = cart.cust_id_id).avl_point
                invoice.m_price = CustomerMembership.objects.get(custid_id = cart.cust_id_id).avl_price
            else:
                invoice.m_point = 0
                invoice.m_price = 0
        invoice.payment_type = 0
        invoice.paid = 0
        invoice.payment_status = 0
        invoice.status = 'Pending'
        invoice.save()
        itemprice = ItemPrice.objects.all()
        inv_cart = Cart.objects.filter(cust_id_id = customer_id).first()
        order_invoice = Invoice.objects.filter(cust_id_id = inv_cart.cust_id_id).last()
        count = 0
        for orders in ocart:
            order = Order()
            for item in itemprice:
                if (orders.service == item.service and orders.product == item.cloth_type and orders.cust_type == item.cust_type):
                    order.ip_id_id = item.id
            order.inv_id_id = order_invoice.id
            order.cust_id_id = orders.cust_id_id
            order.no_item = orders.no_item
            order.cust_type = orders.cust_type
            order.service = orders.service
            order.product = orders.product
            order.ind_price = orders.ind_price
            order.total_price = orders.total_price
            order.remarks = orders.remarks
            order.save()
            count = count+1
            barcode = Barcode()
            barcode.inv_id_id = order_invoice.id
            barcode.cust_id_id = order.cust_id_id
            barcode.bvalue = str(order_invoice.id)+"-"+str(count)
            barcode.service = order.service
            barcode.product = order.product
            barcode.status = order_invoice.cancel
            barcode.remarks = order.remarks
            barcode.save()
        cart_deletes = Cart.objects.filter(cust_id_id = customer_id)
        for cart_delete in cart_deletes:
            cart_delete.delete() 
        detail_id = Invoice.objects.all().last()
        return redirect('order:detail', pk=detail_id.id)
        # return render(request,'order/order_detail.html',{'data':data,"customers":customers})
    return render(request,'order/order_detail.html')


@login_required
def AddToCart(request):
    carts = Cart.objects.all().first()
    customer = Customer.objects.all()
    # customers = Customer.objects.get(pk=carts.cust_id_id)
    itemprice = ItemPrice.objects.all()
    cust_type = set()
    product = set()
    service = set()
    for item in itemprice:
        cust_type.add(item.cust_type)
        product.add(item.cloth_type)
        service.add(item.service)
    if request.method == 'POST':
        detail = request.POST
        if 'name' in detail:
            cart = Cart()
            cart.cust_id_id = detail['customer_name']
            cart.cust_type = detail['type']
            cart.service  = detail['service']
            cart.product = detail['product']
            def item_price(type, service, product):
                itemprice = ItemPrice.objects.all()
                for i in itemprice:
                    if i.cust_type == type and i.service == service and i.cloth_type == product:
                        return i.price
            price = item_price (detail['type'], detail['service'], detail['product'])            
            cart.ind_price = price
            cart.no_item = detail['num_item']
            cart.total_price = int(price) * int(detail ['num_item'])
            cart.remarks = detail['remark']
            cart.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if carts:
        carts= Cart.objects.all().first()
        customers = Customer.objects.get(pk=carts.cust_id_id)
        cart_data = Cart.objects.all()
        total_peice = 0

        total_price = 0

        for cart_total in cart_data:
            total_peice = total_peice+cart_total.no_item
            total_price = total_price+cart_total.total_price
        datas = {
            'name': Customer.objects.get(pk = carts.cust_id_id).customer_name,
            'no_item': total_peice,
            'total_price' : total_price,
            'date':datetime.now().date,
            'due_date': datetime.now()+timedelta(days=5)
        }
        return render(request,'order/order_create.html',{'datas':datas,'customer':customer,'cust_type':cust_type,'service':service,'product':product,'carts':carts,"cart_data":cart_data})
    return render(request,'order/order_create.html',{'carts':carts,'customer':customer,'cust_type':cust_type,'service':service,'product':product})        



# @login_required
# def SaveOrder(request,customer_id):
#     carts = Cart.objects.filter(cust_id_id = customer_id).first()
#     cart_as = Cart.objects.filter(cust_id_id = carts.cust_id_id).first()
#     customers = Customer.objects.get(pk=cart_as.cust_id_id)
#     cartss = Cart.objects.filter(cust_id_id = carts.cust_id_id)   
#     order = Order.objects.filter(cust_id_id = cart_as.cust_id_id).last()
#     if request.method == 'POST':
#         detail = request.POST
#         data = {
#         'date':datetime.now(),
#         'due_date' : datetime.now()+timedelta(days=5),
#         'net_price': detail['net_price'],
#         'discount' : detail['discount'],
#         'discount_type' : detail['discount_type'],
#         'payment_due' : detail['payment_due']
        
#         }
#         # exit()
#         # if 'name' in detail:
#             # if 'payment_type' in detail:
#                 # exit()
#         cart = Cart.objects.all().first()
#         ocart = Cart.objects.all()                
#         invoice = Invoice()
#         invoice.cust_id_id = cart.cust_id_id
#         for item in ocart:
#             invoice.total_piece = invoice.total_piece + item.no_item
#             invoice.price = invoice.price + item.ind_price
#             invoice.net = invoice.net + item.total_price

#         invoice.date = datetime.now()
#         invoice.due_date = datetime.now()+timedelta(days=5)
#         invoice.discount = detail['discount']
#         invoice.payment_due = detail['payment_due']
#         invoice.discount_type =  detail['discount_type']
#         cmbsp = CustomerMembership.objects.all()
#         for cm in cmbsp:
#             if cm.custid_id == cart.cust_id_id:
#                 invoice.m_point = CustomerMembership.objects.get(custid_id = cart.cust_id_id).avl_point
#                 invoice.m_price = CustomerMembership.objects.get(custid_id = cart.cust_id_id).avl_price
#             else:
#                 invoice.m_point = 0
#                 invoice.m_price = 0
#         invoice.payment_type = 0
#         invoice.paid = 0
#         invoice.payment_status = 0
#         invoice.status = 'Pending'
#         # if detail['payment_type'] == '0':
#         #     invoice.payment_type = detail['payment_type']
#         #     invoice.paid = 0
#         #     invoice.payment_status = 0
#         # else:
#         #     invoice.payment_type = detail['payment_type']
#         #     invoice.paid = invoice.payment_due
#         #     invoice.payment_status = 1
#         invoice.save()
#             # exit()
#         itemprice = ItemPrice.objects.all()
#         inv_cart = Cart.objects.all().first()
#         order_invoice = Invoice.objects.filter(cust_id_id = inv_cart.cust_id_id).last()
        
#         count = 0
#         for orders in ocart:
#             order = Order()
#             for item in itemprice:
#                 if (orders.service == item.service and orders.product == item.cloth_type and orders.cust_type == item.cust_type):
#                     order.ip_id_id = item.id
#             order.inv_id_id = order_invoice.id
#             order.cust_id_id = orders.cust_id_id
#             order.no_item = orders.no_item
#             order.cust_type = orders.cust_type
#             order.service = orders.service
#             order.product = orders.product
#             order.ind_price = orders.ind_price
#             order.total_price = orders.total_price
#             order.remarks = orders.remarks
#             order.save()
            
#             count = count+1
#             barcode = Barcode()
#             barcode.inv_id_id = order_invoice.id
#             barcode.cust_id_id = order.cust_id_id
#             barcode.bvalue = str(order_invoice.id)+"-"+str(count)
#             barcode.service = order.service
#             barcode.product = order.product
#             barcode.status = order_invoice.cancel
#             barcode.remarks = order.remarks
#             barcode.save()
#         cart_deletes = Cart.objects.all()
#         for cart_delete in cart_deletes:
#             cart_delete.delete() 
#         detail_id = Invoice.objects.all().last()
#         return redirect('order:detail', pk=detail_id.id)
#         # return render(request,'order/order_detail.html',{'data':data,"customers":customers})
#     return render(request,'order/order_detail.html')

@login_required
def ClearCart(request):
    carts = Cart.objects.all()
    for cart in carts:
        cart.delete()
    return redirect('/order/list/')  

@login_required
def DeleteCart(request,pk):
    carts = Cart.objects.get(pk=pk)
    carts.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def OrderList(request):

    if request.method == 'GET':

        invoice = Invoice.objects.all()
        customer = Customer.objects.all()
        mbsp = CustomerMembership.objects.all()
        
    return render(request, 'order/order_list.html',{'order': invoice,'customer':customer,'mbsp':mbsp})
    

@login_required
def OrderDetail(request, pk):

    if request.method == 'GET':
        
        invoice = Invoice.objects.get(pk=pk)
        customers = Customer.objects.get(pk = invoice.cust_id_id)
        order = Order.objects.filter(inv_id_id = invoice.id)
        customer_name = customers.customer_name
        date = invoice.date
        time = invoice.due_date
        amount = invoice.payment_due
        message = message_data(customer_name,date,time,amount)
        return render(request, 'order/order_detail.html', {'customers':customers,'data':invoice,'order':order,'customer_name':customer_name,'message':message,'customer_name':customer_name,'date':date,'time':time,'amount':amount})

    if request.method == 'POST':
        upd_inv = Invoice.objects.get(pk=pk)
        invoice = Invoice(pk=pk)
        invoice.cust_id_id = upd_inv.cust_id_id
        invoice.date = upd_inv.date
        invoice.due_date = upd_inv.due_date
        invoice.total_piece = upd_inv.total_piece
        invoice.price = upd_inv.price
        invoice.discount = upd_inv.discount
        invoice.net = upd_inv.net
        invoice.payment_due = upd_inv.payment_due
        invoice.m_point = upd_inv.m_point
        invoice.m_price = upd_inv.m_price
        invoice.paid = upd_inv.payment_due
        invoice.payment_due = upd_inv.payment_due      
        def dis_type(net, due_payment, discount):
                    
            if (int(net) -  int(discount) == int(due_payment)):
                return "flat"
            else:
                return "percentage"
        
        invoice.discount_type = dis_type(invoice.net, invoice.payment_due, invoice.discount)
              

        if request.POST['payment_type'] != "0" :
            invoice.payment_status = 1

        invoice.payment_type = request.POST['payment_type']
        invoice.save()
        return redirect('order:list')
    

@login_required
def CancelOrder(request, pk):

    upd_inv = Invoice.objects.get(pk=pk)
    order = Order.objects.filter(inv_id_id = pk)
    invoice = Invoice(pk=pk)
    invoice.cust_id_id = upd_inv.cust_id_id
    invoice.date = upd_inv.date
    invoice.due_date = upd_inv.due_date
    invoice.total_piece = upd_inv.total_piece
    invoice.price = upd_inv.price
    invoice.discount = upd_inv.discount
    invoice.net = upd_inv.net
    invoice.payment_due = upd_inv.payment_due
    invoice.m_point = upd_inv.m_point
    invoice.m_price = upd_inv.m_price
    invoice.paid = upd_inv.payment_due
    invoice.payment_status = 0
    invoice.cancel = 1
    invoice.payment_type = upd_inv.payment_type
    invoice.save()
    invoice = Invoice.objects.all()
    customer = Customer.objects.all()
    mbsp = CustomerMembership.objects.all()
    return render(request, 'order/order_list.html',{'order': invoice,'customer':customer,'mbsp':mbsp})  

@login_required
def OrderUpdate(request, pk):
    itemprice = ItemPrice.objects.all()
    cust_type = set()
    product = set()
    service = set()
    for item in itemprice:
        cust_type.add(item.cust_type)
        product.add(item.cloth_type)
        service.add(item.service)
    invoice = Invoice.objects.get(pk=pk)
    if request.method == 'GET':
        invoice = Invoice.objects.get(pk=pk)
        print(invoice)
        order = Order.objects.filter(inv_id_id = pk)
        print(order)
        itemprice = ItemPrice.objects.all()
        return render(request, 'order/order_update.html', {'order':order,'itemprice':itemprice,'cust_type':cust_type,'service':service,'product':product})
    
    if request.method == 'POST':

        orders = Order.objects.filter(inv_id_id = pk)
        detail = request.POST
        def ipid(type, service, product):
            itemprice = ItemPrice.objects.all()
            for i in itemprice:
                if i.cust_type == type and i.service == service and i.cloth_type == product:
                    return i.id,i.price 
        index = list(range(len(orders)))
        for i,order in zip(index,orders):
            info = {}
            for k,v in detail.lists():
                info[k]= v[i]
            
            item = Order(pk=order.id) 
            item.cust_id_id = order.cust_id_id
            item.inv_id_id = order.inv_id_id
            ip_id,price = ipid (info['type'], info['service'], info['product'])
            item.ip_id_id = ip_id
            item.cust_type = info['type']
            item.service = info['service']
            item.product = info['product']
            item.ind_price = info['price']
            item.no_item = info ['num_item']
            item.total_price =info['net_price']
            item.remarks = info['remark']
            item.save()

        upd_invoice = Invoice(pk=pk)

        upd_invoice.cust_id_id = invoice.cust_id_id
        upd_invoice.date = invoice.date
        upd_invoice.due_date = invoice.due_date
        total_piece = 0
        price = 0
        net = 0
        orders = Order.objects.filter(inv_id_id = pk)
        for item in orders:
            total_piece  = total_piece + item.no_item
            price = price + item.ind_price 
            net = net + item.total_price
        upd_invoice.price = price 
        upd_invoice.net = net
        upd_invoice.total_piece = total_piece
        upd_invoice.discount_type = invoice.discount_type 
        upd_invoice.discount = invoice.discount

        if upd_invoice.discount_type == "flat":
            upd_invoice.payment_due = int(upd_invoice.net) - int(upd_invoice.discount)
        else:
            upd_invoice.payment_due = int(upd_invoice.net) - (int(upd_invoice.net)*int(upd_invoice.discount))/100
        upd_invoice.m_point = invoice.m_point
        upd_invoice.m_price = invoice.m_price
        upd_invoice.payment_type = invoice.payment_type
        upd_invoice.paid = 0
        upd_invoice.save()
       
      
        return redirect('order:detail', upd_invoice.id)

            
@login_required       
def UpdatePayment(request,pk):
    invoice = Invoice.objects.get(pk=pk)
    if request.method=="POST":
        detail = request.POST
        payment_type = detail['payment_type']
        status = detail['status']
        if payment_type == '0':
            invoice.payment_type = '0'
            invoice.paid = 0
            invoice.payment_status = 0
            invoice.status = status
            invoice.save()
            return redirect('order:list')
        else:
            invoice.payment_type = payment_type
            invoice.paid = invoice.payment_due
            invoice.payment_status = 1
            invoice.status = status
            invoice.save()
            return redirect('home:report-order')
        


@login_required
def AddPrice(request):
    itemprice = ItemPrice.objects.all()
    price=0
    if request.method == "POST":
        type = request.POST['type']
        service  = request.POST['service']
        product = request.POST['product']
        for i in itemprice:
            if i.cust_type == type and i.service == service and i.cloth_type == product:
                price = 0+int(i.price)
        return JsonResponse({"price": price}, status=200)
    else:
        # some form errors occured.
        return JsonResponse({"error": ""}, status=400)




@login_required
def InvoiceDetail(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    customers = Customer.objects.get(pk = invoice.cust_id_id)
    order = Order.objects.filter(inv_id_id = invoice.id)

    return render(request, 'order/invoice.html', {'customers':customers,'data':invoice,'order':order})


@login_required
def EmailInvoice(request, pk):
    current_domain = get_current_site(request).domain
    return_file = 'order' + str(pk) + '.pdf'

    invoice = Invoice.objects.get(pk=pk)
    customers = Customer.objects.get(pk = invoice.cust_id_id)
    order = Order.objects.filter(inv_id_id = invoice.id)
    context={'customers':customers,'data':invoice,'order':order,'current_domain':current_domain}
    response = PDFTemplateResponse(request=request,
                                       template='order/email_invoice.html',
                                       filename="Invoice.pdf",
                                       context= context,
                                       show_content_in_browser=True,
                                       cmd_options={'margin-top': 50,},
                                       )
    pdfPath = os.path.join(BASE_DIR,'static/invoice/Invoice.pdf')
    subject = 'Invoice From Hook&Hangers'
    message = "Please Find Your Attachments Below"
    with open(pdfPath, "wb") as f:
        f.write(response.rendered_content)
        mail = EmailMessage(subject, message, EMAIL_HOST_USER, [customers.email])
        mail.attach("Invoice", response.rendered_content, 'application/pdf')
        mail.send()
        if os.path.isfile(pdfPath):
            os.remove(pdfPath)
        return redirect('order:detail', pk)
    return render(request, 'order/invoice.html', {'customers':customers,'data':invoice,'order':order})




@login_required
def WorkshopList(request):

    if request.method == 'GET':
        invoice = Invoice.objects.filter(cancel = 0)
        customers = Customer.objects.all()
        barcode_data = Barcode.objects.all()
        return render(request, 'order/workshop_view.html',{'barcode':barcode_data,'orders':invoice,'customers':customers})

    if request.method == 'POST':
        detail = request.POST
        invoice_data = []
        try:
            info = {}
            for k,v in detail.lists():
                if k == 'invoice_id':
                    info[k]= v
            if 'invoice_id' in info:
                for i in info['invoice_id']:
                    invoice = Invoice.objects.get(pk=i)
                    invoice_data.append(invoice) 
            else:
                return render(request,'cust_barcode/error.html') 
        except IndexError:
            return render(request,'cust_barcode/error.html') 
        customer = Customer.objects.all()
        date = {
            'now':datetime.now().date
        }
        orders = Order.objects.all()
        return render(request,'order/workshop.html',{'invoice_data':invoice_data,'customer':customer,'date':date,'orders':orders})       



