from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_signup_and_profile_creation(self):
        resp = self.client.post(reverse('blog:signup'), {
            'username': 'tester',
            'email': 't@test.com',
            'password1': 'complexpass123',
            'password2': 'complexpass123',
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        user = User.objects.filter(username='tester').first()
        self.assertIsNotNone(user)
        # profile automatically created by signals
        self.assertTrue(hasattr(user, 'profile'))

