
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
        ('Staff', 'Staff'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    

class Admission(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20,null=True, blank=True)
    address = models.CharField(max_length=1000)
    aadhar_number=models.CharField(max_length=15,unique=True, null=True)
    dob = models.DateField(default=timezone.now)
    gender_roles = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")    
    ]
    photo = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=gender_roles)
    date_of_admission = models.DateTimeField(default=timezone.now)
    tenth_id_number = models.CharField(max_length=20)
    tenth_percentage = models.FloatField()
    tenth_marks_sheet = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    twelfth_id_number = models.CharField(max_length=20)
    twelfth_percentage = models.FloatField()
    twelfth_marks_sheet = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    father_name = models.CharField(max_length=225)
    father_email = models.EmailField()
    father_occupation = models.CharField(max_length=225)
    father_phone = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=225)
    mother_occupation = models.CharField(max_length=225)
    
    def __str__(self):
        return self.name

   
from django.db import models

class a(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=20)
