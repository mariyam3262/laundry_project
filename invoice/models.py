from django.db import models
from customer.models import Customer
import datetime





class Invoice(models.Model):
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_piece = models.IntegerField(default=0)
    date = models.DateField()
    due_date = models.DateField()
    price = models.IntegerField(default=0)
    discount_type = models.CharField(max_length=10)
    discount = models.IntegerField(default=0)
    net = models.IntegerField(default=0)
    payment_due = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    payment_type = models.IntegerField(default=0)
    payment_status = models.BooleanField(default=False)
    status = models.CharField(max_length=30,default='Pending')
    cancel = models.BooleanField(default=False)
    m_price = models.IntegerField(default=0)
    m_point = models.IntegerField(default=0)


class ItemPrice(models.Model):
    cust_type = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    cloth_type = models.CharField(max_length=30)
    price = models.CharField(max_length=30)

