from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class User2(User):
    is_donor=models.BooleanField(default=False)

class BloodDonorProfile(models.Model):
    
    user=models.OneToOneField(User2,related_name='blooddonor',on_delete=models.CASCADE)
    donor_name=models.TextField(max_length=30)
    donor_address=models.TextField(max_length=50)
    contact=models.IntegerField(null=True)
    profile_picture=models.ImageField(upload_to='profiles/',null=True)
    qrcode=models.ImageField(upload_to='qrcodes/',null=True)
    choice=(('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-'))
    blood_group=models.CharField(max_length=3,choices=choice,null=True)
    blood_report=models.FileField(upload_to="bloodreports/",null=True)
    def __str__(self):
        return self.donor_name



    