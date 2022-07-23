from django.db import models
from customer.models import Customer
from invoice.models import Invoice,  ItemPrice



class Order(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    inv_id = models.ForeignKey(Invoice, on_delete = models.CASCADE)
    ip_id = models.ForeignKey(ItemPrice, on_delete = models.CASCADE)
    cust_type = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    ind_price = models.IntegerField(default=0)
    no_item = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    remarks = models.CharField(max_length=30)


class Cart(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    cust_type = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    ind_price = models.IntegerField(default=0)
    no_item = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    remarks = models.TextField(default = "None")