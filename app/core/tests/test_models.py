from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with email is successfull"""
        email = "test@gmail.com"
        password = "Pass@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'pass123')

        self.assertEqual(user.email, email.lower())
