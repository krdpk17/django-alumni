from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from django.contrib.auth.forms import UserCreationForm

from .forms import UserProfileForm

import pdb

class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_url_name(self):
        view = resolve('/accounts/signup/')
        print("output is {}".format(view.url_name))
        self.assertEquals(view.url_name, 'signup')

    def test_signup_url_resolves_signup_view_name(self):
        view = resolve('/accounts/signup/')
        print("output is {}".format(view.func))
        self.assertEquals(view.view_name, 'signup')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        profile_form = self.response.context.get('profile_form')
        self.assertIsInstance(form, UserCreationForm)
        self.assertIsInstance(profile_form, UserProfileForm)