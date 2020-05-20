from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=300, blank=True)
    department = models.CharField(max_length=300, blank=True)
    passout_year = models.CharField(max_length=300, blank=True)
    college_name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username 

