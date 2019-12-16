from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User1(User):
    is_hospital=models.BooleanField(default=False)


class HospitalProfile(models.Model):
    user=models.OneToOneField(User1,related_name='hospital',on_delete=models.CASCADE)
    hospital_name=models.TextField(max_length=30)
    hospital_address=models.TextField(max_length=50)
    license=models.FileField(upload_to='documents/')
    profile_picture=models.ImageField(upload_to="hospitalprofiles/",null=True)
    def __str__(self):
        return self.hospital_name
