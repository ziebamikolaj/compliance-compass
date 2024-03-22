import datetime
from django.test import TestCase
from accounts.models import Account
from .models import Organization, Membership
class OrganizationModelTests(TestCase):

    def test_organization_creation(self):
        org = Organization.objects.create(
            name="Test Organization",
            description="This is a test organization",
            location="Some Location"
        )
        self.assertEqual(org.name, "Test Organization")
        self.assertTrue(isinstance(org.date_created, datetime.datetime))  

    def test_str_representation(self):
        org = Organization.objects.create(name="My Organization")
        self.assertEqual(str(org), "My Organization")
class MembershipModelTests(TestCase):
    
    def setUp(self):
        self.user = Account.objects.create(email="example@mail.com", password="testpass")
        self.org = Organization.objects.create(name="Test Organization")
    
    def test_membership_creation(self):
        membership = Membership.objects.create(
            organization=self.org,
            account=self.user,
            role="admin"
        )
        self.assertEqual(membership.role, "admin")
        self.assertTrue(isinstance(membership.date_joined, datetime.datetime))