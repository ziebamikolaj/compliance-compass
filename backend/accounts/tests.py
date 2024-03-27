from django.test import Client, TestCase
from .models import Account
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountModelTests(TestCase):
    def test_email_field_is_valid(self):
        account = User.objects.create_user(
            email="test@example.com", password="testpass"
        )
        self.assertEqual(account.email, "test@example.com")

    def test_is_active_default(self):
        account = User.objects.create_user(
            email="test@example.com", password="testpass"
        )
        self.assertTrue(account.is_active)

    def test_date_joined_auto_now_add(self):
        account = User.objects.create_user(
            email="test@example.com", password="testpass"
        )
        self.assertIsNotNone(account.date_joined)

    def test_account_deletion(self):
        account = User.objects.create_user(
            email="test@example.com", password="testpass"
        )
        account.delete()
        self.assertFalse(Account.objects.filter(email="test@example.com").exists())

    def test_account_update(self):
        account = User.objects.create_user(
            email="test@example.com", password="testpass"
        )
        account.email = "updated@example.com"
        account.save()
        self.assertEqual(account.email, "updated@example.com")

    def test_account_password_change(self):
        account = User.objects.create_user(
            email="test@example.com", password="testpass"
        )
        account.set_password("newpass")
        account.save()
        self.assertTrue(account.check_password("newpass"))

    # constructor tests

    def setUp(self):
        self.client = Client()

    def test_account_creation(self):
        response = self.client.post(
            "/user/register",
            {"email": "test@example.com", "password": "!@#123qweQWE"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_short_password(self):
        response = self.client.post(
            "/user/register",
            {"email": "test@example.com", "password": "123"},  # too short
        )
        self.assertEqual(response.status_code, 400)

    def test_poor_password(self):
        response = self.client.post(
            "/user/register",
            {"email": "test@example.com", "password": "test1234"},  # too basic
        )
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        user = User.objects.create_user(email="test@mail.com", password="123qweQWE")
        user.save()
        response = self.client.post(
            "/user/login",
            {"email": "test@mail.com", "password": "123qweQWE"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue("access" in response.data)
        self.assertTrue("refresh" in response.data)
