from django.db import models
# from django.apps import apps
# apps.get_model('customer.Customer')
from customer.models import Customer


# Create your models here.


class Membership(models.Model):
    service = models.CharField(max_length=20)
    mbsp_amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    validity = models.CharField(max_length=30)


class CustomerMembership(models.Model):
    custid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    msid = models.ForeignKey(Membership, on_delete=models.CASCADE)
    date = models.DateTimeField()
    ex_date = models.DateTimeField()
    avl_price = models.IntegerField(default = 0)
    avl_point = models.IntegerField(default = 0)
    day_ex = models.IntegerField(default = 0)
