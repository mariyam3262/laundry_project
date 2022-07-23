from django.shortcuts import render,redirect
import datetime as dt
# Create your views here.
from django.shortcuts import  render
from customer.models import Customer
from membership.models import Membership, CustomerMembership
import datetime
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required

@login_required
def MembershipListView(request, page=1):
     
     if request.method == 'GET':
        mbsp_detail = Membership.objects.all()
        # paginator = Paginator(mbsp_detail, 1)
        # try:
        #     mbsp_detail = paginator.page(page)
        # except EmptyPage:
        #     mbsp_detail = paginator.page(paginator.num_pages)

        return render(request,'membership/membership_list.html',{'mbsp_detail':mbsp_detail})


@login_required
def MemebershipCreateView(request):

    if request.method == 'GET':        
        return render(request,'membership/membership_create.html')

    if request.method == 'POST':
        detail = request.POST
        membership = Membership()
        membership.service = detail['service']
        membership.price = detail['price']
        membership.point = detail['point']
        membership.validity = detail['validity']
        membership.mbsp_amount = detail['amount']
        membership.save()
        return redirect('mbsp:mbsp-list')

@login_required
def MenbershipDetailView(request, pk):
    mbsp = Membership.objects.get(pk=pk)
    return render(request, 'membership/membership_detail.html',{'mbsp':mbsp})


@login_required
def MembershipUpdateView(request, pk):
    

    if request.method == 'GET':
        mbsp = Membership.objects.get(pk=pk)
        return render(request, 'membership/membership_update.html',{'mbsp':mbsp})

    if request.method == 'POST':
        detail = request.POST
        membership = Membership(pk=pk)
        membership.service = detail['service']
        membership.price = detail['price']
        membership.point = detail['point']
        membership.validity = detail['validity']
        membership.mbsp_amount = detail['amount']
        membership.save()
        mbsp = Membership.objects.get(pk=pk)

        return render(request,'membership/membership_detail.html',{'mbsp':mbsp})

@login_required
def MembershipDeleteView(request, pk):

    if request.method == 'GET':
        Membership(pk=pk).delete()
    return redirect('mbsp:mbsp-list')

@login_required
def CustMbspCreateView(request):

    if request.method == 'GET':
        customer = Customer.objects.all()
        mbsp_detail = Membership.objects.all()
        return render(request, 'membership/custmbsp_create.html', {'customer':customer, 'mbsp_detail':mbsp_detail})

    if request.method == 'POST':

        detail = request.POST
        custmbsp = CustomerMembership()
        custmbsp.custid_id = detail['cust_id']
        custmbsp.msid_id = detail['msid']
        custmbsp.date = detail['date']
        custmbsp.ex_date = detail['ex_date']
        custmbsp.avl_point = detail['point']
        custmbsp.avl_price = detail['price']
        def days(ex_date):
            today = dt.datetime.now().date()
            date = dt.datetime.strptime(ex_date, '%Y-%m-%d').date()
            exdate =  date - today 
            return exdate 
        custmbsp.day_ex = days(detail['ex_date']).days
        custmbsp.save()
        return redirect('mbsp:cmbsp-list')

@login_required        
def CustMbspListView(request, page=1):

    if request.method == 'GET':
        cmbsp_data = CustomerMembership.objects.all()
        mbsp =Membership.objects.all()
        # paginator = Paginator(cmbsp_data, 1)
        # try:
        #     cmbsp_data = paginator.page(page)
        # except EmptyPage:
        #     cmbsp_data = paginator.page(paginator.num_pages)
    return render(request, 'membership/custmbsp_list.html',{'cmbsp_data':cmbsp_data,'mbsp':mbsp}) 

@login_required
def CustMbspDetailView(request, pk):

    if request.method == 'GET':
        cmbsp_data = CustomerMembership.objects.get(pk=pk)
        return render(request, 'membership/custmbsp_detail.html', {'cmbsp_data':cmbsp_data})

@login_required
def CustMbspDeleteView(request, pk):

    if request.method == 'GET':
        data = CustomerMembership(pk=pk)
        data.delete()
        return redirect('mbsp:cmbsp-list')

@login_required
def CustMbspUpdateView(request, pk):

    if request.method == 'GET':
            customer = Customer.objects.all()
            mbsp_detail = Membership.objects.all()
            cmbsp= CustomerMembership.objects.get(pk=pk)
            return render(request, 'membership/custmbsp_create.html', {'customer':customer, 'mbsp_detail':mbsp_detail ,'cmbsp':cmbsp})

    if request.method == 'POST':

        detail = request.POST
        custmbsp = CustomerMembership(pk=pk)
        custmbsp.custid_id = detail['cust_id']
        custmbsp.msid_id = detail['msid']
        custmbsp.date = detail['date']
        custmbsp.ex_date = detail['ex_date']
        custmbsp.avl_price = detail['price']
        custmbsp.avl_point = detail['point']
        def days(ex_date):
            today = dt.datetime.now().date()
            date = dt.datetime.strptime(ex_date, '%Y-%m-%d').date()
            exdate =  date - today 
            return exdate 
        
            


        custmbsp.day_ex = days(detail['ex_date']).days
        custmbsp.save()
        
        return redirect('mbsp:cmbsp-detail', pk)
