from django.db import models
from django.contrib.auth.models import User
import datetime

YEAR_CHOICES = []
for r in range(1930, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

  
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField()
    passout_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    course = models.CharField( max_length = 20)
    linkedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True) 
    def __str__(self):
        return self.user.username 

