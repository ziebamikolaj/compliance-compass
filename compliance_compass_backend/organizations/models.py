from django.db import models

from accounts.models import Account

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(Account, through='Membership') 
      

class Membership(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)  # Assuming 'Account' model exists
    # You can add extra fields if needed, like:
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.username