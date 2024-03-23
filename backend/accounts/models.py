from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

 

    def __str__(self):
        return self.email