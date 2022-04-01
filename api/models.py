from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=15)
    address=models.TextField(max_length=50)
    verify=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name