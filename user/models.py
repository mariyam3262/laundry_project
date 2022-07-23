from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password_confirm = models.CharField(max_length=255,default=0)
    email = models.EmailField(max_length=200)
    m_number = models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True) 
    

