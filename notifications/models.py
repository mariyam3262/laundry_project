from django.db import models
from user.models import  User
class Notification(models.Model):
    
    Class=models.CharField(max_length=50)
    key=models.CharField(max_length=100)
    message=models.TextField(max_length=500)
    route=models.CharField(max_length=200)
    # seen=models.
    # read=models.
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # created_at=models


class Text(models.Model):
    text = models.TextField(null = True)