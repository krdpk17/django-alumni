from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

import pdb

class SignUpTests(TestCase):
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