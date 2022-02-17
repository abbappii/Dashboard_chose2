
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(decimal_places=2, max_digits=5, default=500.00)
    phone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=255, null = True, blank=True)


# 

    

