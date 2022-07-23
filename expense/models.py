from django.db import models
import datetime
# Create your models here.



class Expense(models.Model):
    expense = models.TextField()
    date = models.DateField()
    amount = models.CharField(max_length=30,default =0)
    remarks = models.TextField(default = "None")