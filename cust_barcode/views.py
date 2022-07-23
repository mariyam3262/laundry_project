from csv import writer
from datetime import datetime
from django.shortcuts import render,redirect
from cust_barcode.models import Barcode
from customer.models import Customer
from django.http import Http404
import barcode
from barcode.writer import ImageWriter
from invoice.models import Invoice
import os
from hooks.settings import BASE_DIR
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
# from xhtml2pdf.pdf import render_to_pdf_response

# Create your views here.
@login_required
def BarcodeList(request):

    if request.method == 'GET':
        invoice = Invoice.objects.filter(cancel = 0)
        barcode_data = Barcode.objects.all()
        return render(request, 'cust_barcode/barcode_list.html',{'barcode':barcode_data,'orders':invoice})

    if request.method == 'POST':
        detail = request.POST
        barcode_data = []
        try:
            info = {}
            for k,v in detail.lists():
                if k == 'bar_id':
                    info[k]= v
            if 'bar_id' in info:
                for i in info['bar_id']:
                    bar = Barcode.objects.get(pk= i)
                    cust = Customer.objects.get(pk = bar.cust_id_id)
                    EAN = barcode.get_barcode_class('code128')
                    ean = EAN(f'{bar.bvalue}',writer = ImageWriter())
                    ean.save(os.path.join(BASE_DIR,'static/images/' + f'{bar.id}'))
                    barcode_data.append(bar)
            else:
                return render(request,'cust_barcode/error.html') 
        except IndexError:
            return render(request,'cust_barcode/error.html') 
        customer = Customer.objects.all()
        date = {
            'now':datetime.now().date
        }
        invoice = Invoice.objects.all()
        return render(request,'cust_barcode/barcode_view.html',{'barcode_data':barcode_data,'customer':customer,'date':date,'invoice':invoice})       

@login_required
def OrderBarcode(request, pk):
    barcode_data = []
    invoice = Invoice.objects.filter(id = pk)
    bar = Barcode.objects.filter(inv_id_id= pk)
    for i in bar:
        EAN = barcode.get_barcode_class('code128')
        ean = EAN(f'{i.bvalue}',writer = ImageWriter())
        ean.save(os.path.join(BASE_DIR,'static/images/' + f'{i.id}'))
        barcode_data.append(i)
    customer = Customer.objects.all()
    date = {
        'now':datetime.now().date
    }
    invoice = Invoice.objects.all()
    return render(request,'cust_barcode/barcode_view.html',{'barcode_data':barcode_data,'customer':customer,'date':date,'invoice':invoice}) 










         
# @login_required
# def ReadBarcode(request):
#     barcode = Barcode.objects.all()
#     customer = Customer.objects.all()
#     return render(request, 'cust_barcode/workshop.html',{'barcode':barcode,'customer':customer})