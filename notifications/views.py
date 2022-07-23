from email import message
from django.shortcuts import render, redirect
from notifications.models import Text
# import pywhatkit
from django.core.mail import send_mail,EmailMessage
from customer.models import Customer
from invoice.models import Invoice
from django.contrib.auth.decorators import login_required


def message_data(customer_name,date,time,amount):
    message = Text.objects.all().first()
    data = [customer_name,date,time,amount]
    messages = message.text.format(*data)
    return messages     

# @login_required
# def GuiView(request):
#     if request.method == 'GET':
#          pywhatkit.sendwhatmsg("+917698720994", "'dear , Thank you for placing an order Your order with Garment The total amount is The order is expected to be ready on . Cheers! Thanks Hooks and Hangersnnnn",21,59)
#     return render(request,'notifications/msg_list.html')

@login_required        
def WhatsappMessageListView(request): 
    if request.method == 'GET':
        message = Text.objects.all().first()
        return render(request,'notifications/msg_list.html',{'message':message})

    if request.method == 'POST':
        return redirect('notifications:what_update')

@login_required
def WhatsappMessageView(request):
    if request.method == 'GET':
        message = Text.objects.all().first()
        return render(request,'notifications/msg_view.html',{'message':message})


@login_required
def  WhatsappMessageUpdateView(request):
    if request.method == 'GET':
        message = Text.objects.all().first()
        return render(request,'notifications/msg_update.html',{'message':message})


    if request.method == 'POST':
        message = Text.objects.all().first()
        message.text = request.POST['message']
        message.save()
        return redirect('notifications:what_list')
    # return render(request,'notifications/msg_list.html',{'message':message})
@login_required   
def  NotificationListView(request):
     if request.method == 'GET':
        message = Text.objects.all().first()
        return render(request,'notifications/notification.html')
        
@login_required
def SendEmail(request, pk,customer_name,date,time,amount):  
    data = [customer_name,date,time,amount]
    inv = Invoice.objects.get(pk=pk)
    cust = Customer.objects.get(id = inv.cust_id_id)
    cust_mail = cust.email
    message = Text.objects.all().first()
    send_mail(
        'This Mail Is From HooksandHangers',
        message.text.format(*data),
        'tataskytv65@gmail.com',
        [cust_mail],
        fail_silently=False,
    )
    return redirect('order:detail', pk)