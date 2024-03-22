
from django.test import TestCase
from .models import Account

class AccountModelTests(TestCase):
    def test_email_field_is_valid(self):
        account = Account.objects.create(email="test@example.com", password="testpass")
        self.assertEqual(account.email, "test@example.com")
    
    def test_password_field_max_length(self):
        with self.assertRaises(Exception):
            # Password exceeding 100 characters should raise an error
            Account.objects.create(email="test@example.com", password="a" * 101)

    def test_is_active_default(self):
        account = Account.objects.create(email="test@example.com", password="testpass")
        self.assertTrue(account.is_active)

    def test_date_joined_auto_now_add(self):
        account = Account.objects.create(email="test@example.com", password="testpass")
        self.assertIsNotNone(account.date_joined)

    def test_str_representation(self):
        account = Account.objects.create(email="test@example.com", password="testpass")
        self.assertEqual(str(account), "test@example.com") 

    def test_account_deletion(self):
        account = Account.objects.create(email="test@example.com", password="testpass")
        account.delete()
        self.assertFalse(Account.objects.filter(email="test@example.com").exists())

    def test_account_update(self):
        account = Account.objects.create(email="test@example.com", password="testpass")
        account.email = "updated@example.com"
        account.save()
        self.assertEqual(account.email, "updated@example.com")

    def test_account_password_change(self):
        account = Account.objects.create(email="test@example.com", password="testpass")
        account.set_password("newpass")  # This is how you change a password
        account.save()
        self.assertTrue(account.check_password("newpass"))  # This should return True