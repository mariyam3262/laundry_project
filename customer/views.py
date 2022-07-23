from re import template
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Customer
from order.models import Order
from invoice.models import ItemPrice,Invoice
from membership.models import CustomerMembership
import datetime as dt
from django.contrib.auth.decorators import login_required
#It will list the info of customers 

@login_required
def CustomerListView(request):

    if request.method == 'GET':
        custs = Customer.objects.all()
        return render(request, 'customer/customer_list.html',{'custs':custs})

#For Creation of new customer
@login_required
def CustomerCreateView(request):

    #Return registration form
    if request.method == 'GET':
        return render(request, 'customer/customer_create.html')

    #Add new customer and redirect to list-page
    if request.method == 'POST':

        context = request.POST
        customer = Customer()
        customer.customer_name = context['name']
        customer.mobile = context['mobile']
        customer.address = context['address']
        customer.location = context['location']
        customer.email = context['email']
        customer.pincode = context['pincode']
        if context['dob'] == '' or context['dob'] == None:
            customer.dob = None
        else:
            customer.dob = context['dob']
        customer.otp = context['otp']
        customer.customer_service = context['service']
        customer.customer_status = context['status']
        customer.customer_type = context['cust_type']
        customer.save()
        custs = Customer.objects.all()
        return redirect('customer:list')


#Show the detail of the individual customer using ID
@login_required
def CustomerDetailView(request, pk):

    if request.method == 'GET':
        cust_detail = Customer.objects.get(pk=pk)
        return render(request, 'customer/customer_detail.html', {'cust_detail':cust_detail})
#Delete the customer 
@login_required
def CustomerDeleteView(request, pk):
    
    if request.method == 'GET':
        delete_record = Customer(pk=pk)
        delete_record.delete()

    return redirect('customer:list')


@login_required
def CustomerUpdateView(request,pk):
    if request.method == 'GET':
        cust= Customer.objects.get(pk=pk)
        return render(request, 'customer/customer_update.html',{'cust':cust})
    if request.method == 'POST':
        cust= Customer.objects.get(pk=pk)
        context_data = request.POST
        cust_detail = Customer(pk=pk)
        cust_detail.customer_name = context_data['name']
        cust_detail.mobile = context_data['mobile']
        cust_detail.address = context_data['address']
        cust_detail.location = context_data['location']
        cust_detail.email = context_data['email']
        cust_detail.pincode = context_data['pincode']
        cust_detail.dob = context_data['dob']
        cust_detail.otp = context_data['otp']
        cust_detail.register_date = cust.register_date 
        cust_detail.customer_service = context_data['service']
        cust_detail.customer_status = context_data['status']
        cust_detail.customer_type = context_data['cust_type']
        cust_detail.save()  
        return redirect('customer:list')



@login_required
def ActiveCustomer(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    today = dt.date.today() # if date is 01/01/2018
    year, week_num, day_of_week = today.isocalendar()
    custs = []
    active_list = set()
    inactive_list = set()
    onstore = 0
    for cust in customer:
        invoice = Invoice.objects.filter(cust_id_id = cust.id)
        if cust.customer_type == 'onstore':
            onstore = onstore + 1
        flag = 0
        for order in invoice:
           
            if order.payment_status == 1:
                nyear, nweek_num, day_of_week = order.date.isocalendar()
                if year == nyear and week_num == nweek_num:
                    flag = flag + 1
        if flag >= 2 :
            active_list.add(cust)
        else:
            inactive_list.add(cust)
    for a in active_list:
        custs.append(a)
    return render(request, 'customer/active_customer.html',{'custs':custs})

@login_required
def UnactiveCustomer(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    today = dt.date.today() # if date is 01/01/2018
    year, week_num, day_of_week = today.isocalendar()
    custs = []
    active_list = set()
    inactive_list = set()
    onstore = 0
    for cust in customer:
        invoice = Invoice.objects.filter(cust_id_id = cust.id)
        if cust.customer_type == 'onstore':
            onstore = onstore + 1
        flag = 0
        for order in invoice:
           
            if order.payment_status == 1:
                nyear, nweek_num, day_of_week = order.date.isocalendar()
                if year == nyear and week_num == nweek_num:
                    flag = flag + 1
        if flag >= 2 :
            active_list.add(cust)
        else:
            inactive_list.add(cust)
    for a in inactive_list:
        custs.append(a)
    return render(request, 'customer/inactive_customer.html',{'custs':custs})