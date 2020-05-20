from django.db import models
from django.contrib.auth.models import User

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
  
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #course = models.CharField(max_length=300, blank=True)
    department = models.CharField(max_length=300, blank=True)
    passout_year = models.DateField(max_length=300, blank=True)
    college_name = models.CharField(max_length=300, blank=True)
    course = models.CharField( 
        max_length = 20, 
        choices = COURSE_CHOICES
        ) 
    def __str__(self):
        return self.user.username 

