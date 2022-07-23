from django.shortcuts import render
from customer.models import Customer
from order.models import Order
from invoice.models import ItemPrice,Invoice
from membership.models import CustomerMembership
import datetime as dt
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import datetime

end = datetime.today()
start = datetime(end.year, end.month, 1)


def index(request):
    return render(request, 'home/dashboard.html')

@login_required
def dashboard(request):
    customer = Customer.objects.all()

    birth_day = []
    for cust in customer:
        if cust.dob == dt.date.today():
            birth_day.append(cust)

    order = Order.objects.all()
    today = dt.date.today() # if date is 01/01/2018
    year, week_num, day_of_week = today.isocalendar()

    active_list = set()
    inactive_list = set()
    onstore = 0
    total = len(customer)

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

    
    cutomer_detail = {
        'active': len(active_list),
        'inactive' : len(inactive_list),
        'onstore' : total ,
        'total' : total,

    }
    daily = 0
    weekly = 0 
    monthly = 0
    orders = Order.objects.all()
    invoices = Invoice.objects.all()
    for order in invoices:
        # invoice = Invoice.objects.get(pk=order.inv_id_id)
        thedate = order.date
        nyear, nweek, nday = thedate.isocalendar()
        if order.paid != 0:
            if thedate == today:
                daily = daily + 1
               
            if year == nyear and nweek ==  week_num:
                weekly = weekly + 1
               
            if year == nyear and thedate.month == today.month:               
                monthly = monthly + 1
    order_report = {
        'today': dt.date.today() ,
        # 'week': ,
        # # 'month':month,
        'daily' : daily,
        'weekly' : weekly,
        'monthly': monthly,
        
    }
    labels = list()
    data  = list() 
    items = ItemPrice.objects.all()
    service_wise = list()
    for item in items :
        i_count = 0 
        item_data = {}
        for order in orders:
            inv_paid = Invoice.objects.get(id=order.inv_id_id)
            if order.service == item.service and order.product == item.cloth_type and order.cust_type == item.cust_type and inv_paid.payment_status == 1:
                i_count = i_count + 1

        item_data['service'] = item.service
        item_data['product'] = item.cloth_type
        item_data['cust_type'] = item.cust_type
        item_data['total'] = i_count
        labels.append(item.service)
        data.append(i_count)        
        service_wise.append(item_data)
    
    item = ItemPrice.objects.all()
    return render(request, 'home/dash_dashboard.html',{'birth_day':birth_day,'customer':customer,'order':order,'count':cutomer_detail,'service_wise':service_wise,'order_report':order_report,'labels':labels,'data':data,'item':item})



@login_required
def OrderReport(request):

    invoice = Invoice.objects.all().order_by('-id').values()
    customer = Customer.objects.all()
    order = Order.objects.all()
    cmbsp = CustomerMembership.objects.all()
    current_month_orders = Invoice.objects.filter(date__gte=str(start.strftime("%Y-%m-%d")),date__lte=str(end.strftime("%Y-%m-%d")))
    print(current_month_orders)
    print(start.strftime("%Y-%m-%d"))
    print(end.strftime("%Y-%m-%d"))
    return render(request, 'home/report_order.html',{'invoice':invoice,'customer':customer,'orders':order,'cmbsp':cmbsp,'current_month_orders':current_month_orders})

@login_required
def CancelReport(request):
    invoice = Invoice.objects.all()
    customer = Customer.objects.all()
    order = Order.objects.all()
    cmbsp = CustomerMembership.objects.all()
    return render(request, 'home/cancel_order.html',{'invoice':invoice,'customer':customer,'orders':order,'cmbsp':cmbsp})
