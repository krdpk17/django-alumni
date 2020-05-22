from django.contrib.auth.models import User
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

    def test_form_inputs(self):
        '''
        The view must contain five inputs: csrf, username, email,
        password1, password2
        '''
        self.assertContains(self.response, '<input', 12)
        self.assertContains(self.response, 'type="text"', 4)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)
        self.assertContains(self.response, 'type="url"', 4)

class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'test',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456',
            'email': 'test@test.com',
            'birth_date_month': '1',
            'birth_date_day': '1',
            'birth_date_year': '1990',
            'passout_year': '2000',
            'course': 'UG1'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())