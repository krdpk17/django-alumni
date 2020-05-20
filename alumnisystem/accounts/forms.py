from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse_lazy
import datetime

COURSE_CHOICES = [
    ('UG', (
            ('UG1', 'B-MATH'),
            ('UG2', 'B-STAT'),
        )
    ),
    ('PG', (
            ('PG1', 'M-MATH'),
            ('PG2', 'M-STAT'),
            ('PG6', 'MTech-CS'),
            ('PG7', 'MTech-CRS'),
            ('PG8', 'MTech-QROR'),
            ('PG3', 'MS-QE'),
            ('PG4', 'MS-LIS'),
            ('PG5', 'MS-QMS')
        )
    ),
    ('PHD', (
            ('PHD1', 'Stats'),
            ('PHD2', 'Maths'),
            ('PHD3', 'QE'),
            ('PHD4', 'CS'),
            ('PHD5', 'QROR'),
            ('PHD6', 'Physics'),
            ('PHD7', 'Geology'),
            ('PHD8', 'Bilogy'),
            ('PHD9', 'LIS')
        )
    ),
    ('Diploma', (
            ('D1', 'PGDBA'),
            ('D2', 'Stats'),
            ('D3', 'Computers')
        )
    ),
    ('unknown', 'Unknown'),
]

'''
Section for signup data
'''
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')            

class UserProfileForm(forms.ModelForm):
    cur_year = datetime.datetime.today().year
    year_range = tuple([i for i in range(cur_year - 90, cur_year - 20)])
    course = forms.MultipleChoiceField(choices = COURSE_CHOICES)
    birth_date = forms.DateField(initial=datetime.date.today() - datetime.timedelta(days=365*30),widget=forms.SelectDateWidget(years=year_range))
    
    class Meta:
        model = UserProfile
        exclude = ['user']

    def clean_course(self):
        courses = self.cleaned_data['course']
        if not courses:
            raise forms.ValidationError("...")

        if len(courses) > 2:
            raise forms.ValidationError("...")

        courses = ' '.join(courses)
        return courses


'''
Section for update data
'''
class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EditUserProfileForm(forms.ModelForm):
    """
    This class is a carbon copy of the UserChangeForm class from
    django.contrib.auth.forms, with the password functionality deleted, and
    the form is modified to allow changes to be made to the
    UserProfle, which extends the Django User
    """
    class Meta:
        model = UserProfile
        success_url = reverse_lazy('update')
        exclude = ['user', 'course', 'birth_date', 'passout_year']

    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
