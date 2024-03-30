'''
Test cases for models
'''
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_success(self):
        email = 'test@example.com'
        password = 'Pass123$'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized_success(self):
        test_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['teST4@ExAMPle.COM', 'teST4@example.com'],
        ]

        for email, expected_email in test_emails:
            user = get_user_model().objects.create_user(email, 'pass123$')
            self.assertEqual(user.email, expected_email)

    def test_new_user_empty_email_raise_valueerror(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'pass123$',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
