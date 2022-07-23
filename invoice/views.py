from django.shortcuts import render,redirect
from invoice.models import ItemPrice
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required


@login_required
def ItemListView(request, page=1):
    
    if request.method == 'GET':
        items= ItemPrice.objects.all()
        return render(request, 'invoice/item_list.html', {'items':items})


@login_required
def ItemCreateView(request):

    if request.method =='GET':
        return render(request, 'invoice/item_create.html')

    if request.method =='POST':
        detail = request.POST
        item = ItemPrice()
        item.cust_type = detail['type']
        item.service = detail['service']
        item.cloth_type = detail['cloth_type']
        item.price = detail['price']
        item.save()
        return redirect('invoice:list')

@login_required
def ItemDetailView(request, pk):

    if request.method == 'GET':
        items= ItemPrice.objects.get(pk=pk)
        return render(request, 'invoice/item_detail.html',{'items':items})

@login_required
def ItemUpdateView(request, pk):

    if request.method == 'GET':
        items = ItemPrice.objects.get(pk=pk)
        return render(request, 'invoice/item_update.html',{'items':items})
    
    if request.method == 'POST':
        detail = request.POST
        item = ItemPrice(pk=pk)
        item.cust_type = detail['type']
        item.service = detail['service']
        item.cloth_type = detail['cloth_type']
        item.price = detail['price']
        item.save()
        return redirect('invoice:detail', pk)


@login_required
def ItemDeleteView(request, pk):

    if request.method == 'GET':
        item = ItemPrice(pk=pk)
        item.delete()
    return redirect('invoice:list')
