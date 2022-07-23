from django.db import models
# from membership.models import CustomerMembership,CustomerMembership

class Customer(models.Model):
    customer_name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    location = models.CharField(max_length = 150)
    email = models.EmailField(max_length=100 , blank=True)
    pincode = models.IntegerField(default=0)
    dob = models.DateField(blank=True, null=True, default=None)
    # memebership_id = models.ForeigneKey(CustomerMembership, on_delete=True)
    otp = models.IntegerField(default=0)
    customer_service = models.CharField(max_length=30)
    customer_status = models.BooleanField(default=False)
    customer_type = models.CharField(max_length=20)
    register_date = models.DateField(auto_now_add=True) 

