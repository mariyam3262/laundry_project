from django.db import models
from customer.models import Customer
from invoice.models import Invoice,ItemPrice

# Create your models here.

class Barcode(models.Model):
    inv_id=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    cust_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    bvalue=models.CharField(max_length=100)
    service=models.CharField(max_length=20)
    product=models.CharField(max_length=20)
    status=models.BooleanField(default=0)
    remarks=models.CharField(max_length=200)
