import pdb
from django.test import TestCase
from ..forms import SignUpForm, UserProfileForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        profile_form = UserProfileForm()
        form_expected = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        profile_form_expected = ['bio', 'location', 'birth_date', 'passout_year', 'course', 
                                    'linkedin_url', 'facebook_url', 'twitter_url', 'github_url', 'website_url']
        form_actual = list(form.fields)
        profile_form_actual = list(profile_form.fields)
        self.assertSequenceEqual(form_expected, form_actual)
        self.assertSequenceEqual(profile_form_expected, profile_form_actual)