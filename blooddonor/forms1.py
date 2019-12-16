from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.db import transaction
from .models import BloodDonorProfile,User2
import pyqrcode
from django.core.files import File
from cv2 import imread 
from os import remove
class SignUpForm(UserCreationForm):
    #username1=forms.CharField(label="username",max_length=10,widget=forms.TextInput(attrs={'id':'username1','name':'username1'}))
    donor_name=forms.CharField(max_length=30)
    contact=forms.IntegerField()
    #another=forms.FileField()
    donor_city=forms.CharField(max_length=30)
    #license=forms.FileField(required=False,widget=forms.FileInput(attrs={'id':'license','name':'license'}))
    profile_picture=forms.FileField(required=False,widget=forms.FileInput(attrs={'id':'profile_picture','name':'profile_picture'}))
    class Meta(UserCreationForm.Meta):
        model=User2
        #model=BloodDonorProfile
        fields=('donor_name','donor_city','contact','username','profile_picture')
        
        
    @transaction.atomic
    def save(self,file, commit=True):
        with transaction.atomic():
            user1 = super().save(commit=False)
            user1.is_donor=True
            #user.refresh_from_db()  # very important! this will load the profile instance created by the signal
            user1.save()
            blooddonorprofile=BloodDonorProfile.objects.create(user=user1)
            blooddonorprofile.donor_name = self.cleaned_data.get('donor_name')
            blooddonorprofile.donor_address = self.cleaned_data.get('donor_city')
            blooddonorprofile.contact=self.cleaned_data.get('contact')
            blooddonorprofile.profile_picture=file
            #print(blooddonorprofile.id)
            big_code = pyqrcode.create(str(blooddonorprofile.id), error='L', version=27, mode='binary')
            big_code.png(str(blooddonorprofile.id)+".png", scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
            with open(str(blooddonorprofile.id)+".png","rb") as destination_file:
                blooddonorprofile.qrcode.save(str(blooddonorprofile.id)+".png",File(destination_file),save=False)
            #blooddonorprofile.qrcode=imread(str(blooddonorprofile.id)+".png")
            #print(user.blooddonorprofile.donor_address,user.blooddonorprofile.contact)
            #user.hospitalprofile.license=self.cleaned_data.get('license')
            #print("hospital license",user.hospitalprofile.license)
            # set here all other values
            try:
                os.remove(str(blooddonorprofile.id)+".png")
            except:
                pass
            blooddonorprofile.save()
            return user1

