from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='documents')
    uploaded_file = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.title