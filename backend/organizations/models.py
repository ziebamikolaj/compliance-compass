from django.db import models
from accounts.models import Account


class Organization(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the organization's name")
    description = models.TextField(
        help_text="Enter a brief description of the organization"
    )
    location = models.CharField(
        max_length=100, help_text="Enter the organization's location"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(
        Account, through="Membership", related_name="organizations"
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    ROLES = (
        ("member", "Member"),
        ("admin", "Admin"),
    )

    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="memberships"
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="memberships"
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, blank=True, choices=ROLES)

    def __str__(self):
        return self.account.email
