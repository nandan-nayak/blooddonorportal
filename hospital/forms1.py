from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.db import transaction
from .models import HospitalProfile,User1
class SignUpForm(UserCreationForm):
    #username1=forms.CharField(label="username",max_length=10,widget=forms.TextInput(attrs={'id':'username1','name':'username1'}))
    hospital_name=forms.CharField(max_length=30)
    
    #another=forms.FileField()
    hospital_address=forms.CharField(max_length=30)
    license=forms.FileField(widget=forms.FileInput(attrs={'id':'license','name':'license'}))
    profile_picture=forms.FileField(required=True,widget=forms.FileInput(attrs={'id':'profile_picture','name':'profile_picture'}))
    class Meta(UserCreationForm.Meta):
       model=User1
        #model=HospitalProfile
       fields=('hospital_name','hospital_address','license','username','profile_picture')
        
        
    @transaction.atomic
    def save(self,file,file1, commit=True):
        with transaction.atomic():
            
            user = super().save(commit=False)
            user.is_hospital=True
            #user.refresh_from_db()  # very important! this will load the profile instance created by the signal
            user.save()
            #print("forms save")
            #user.username=self.cleaned_data.get('username')
            #user.raw_password=self.cleaned_data.get('password1')
            #print(dir(user))
            hospitalprofile=HospitalProfile.objects.create(user=user)
            hospitalprofile.profile_picture=file1
            #print("formsw ",hospitalprofile.license)
            hospitalprofile.hospital_name=self.cleaned_data.get('hospital_name')
            hospitalprofile.hospital_address=self.cleaned_data.get('hospital_address')
            hospitalprofile.license=file
            #print(" hospital name is ",self.cleaned_data.get('hospital_name'))
            hospitalprofile.save()
            return user


class FileUpload(forms.ModelForm):
    class Meta:
        model=HospitalProfile
        fields=('license',)