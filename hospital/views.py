from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms1 import SignUpForm,FileUpload
from django.db.models import ImageField
from .forms2 import DonorUpdate,DonorReport
from cv2 import imread,imwrite
from blooddonor.models import  BloodDonorProfile as bdp 
from django.http import JsonResponse
import time
from PIL import Image,ImageFile
from pyzbar.pyzbar import decode
ImageFile.LOAD_TRUNCATED_IMAGES = True
# Create your views here.

from .forms import UserLoginForm


def hospitallogin(request):
    context=dict()
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid() :
        
        #print("entered into login")
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        #print("request us ",request.user.user1.hospital)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('hospitalhome')
    context['form']= form

    
    if request.method=='POST':
        #print("POST method")
        
        form1=SignUpForm(request.POST,request.FILES) 
        #form2=FileUpload(request.FILES)
        #print(dir(form1.save()))
        #print("form1 ===",form1.is_valid())
        if form1.is_valid() :
            #print("the   license fileo is ",request.FILES['license'])
            user=form1.save(file=request.FILES['license'],file1=request.FILES['profile_picture'])
            print("views valid")
            #user=form2.save()
            #user.refresh_from_db()
            #print("views.py",user.hospitalprofile.hospital_name)
            #user.hospitalprofile.hospital_name = form1.cleaned_data.get('hospital_name')
            #user.hospitalprofile.hospital_address = form1.cleaned_data.get('hospital_address')
            
            #user.save()
            #print('hospitalprofile' in dir(user))
            #print('hospital name ',form1.save().hospitalprofile.hospital_name)
            #print('hospital address ',dir(form1.save().hospitalprofile))
            #username=form1.cleaned_data.get('username1')
            raw_password=form1.cleaned_data.get('password1')
            #name=form1.cleaned_data.get('hospital_name')
            #print(username)
            #print(" username is ",form1.save().username)
            #print(" password is ",user.password)
            
            #print(name)
            
            #user=authenticate(user=user.username,password=raw_password)
            #print("dir====",dir(user))
            #login(request,user)
            #user = authenticate(username=user.username, password=user.password)
            print("hospital name = ",user.user1.hospital.hospital_name)
            login(request, user)
            return redirect('hospitalhome')
        
    else:
        form1=SignUpForm()
        #form2=FileUpload()
    context['form1']=form1
    #context['form2']=form2
    return render(request,'loginpage.html',context)




def home(request):
   
    context=dict()
    if request.method=="POST":
        print("request",request.POST)
        #form2=DonorUpdate(request.POST,request.FILES)
        #form3=DonorReport(request.POST,request.FILES)
        
        if 'qrbutton' in list(request.POST.keys()):
            print("qrcode");
            x=request.FILES['qrcodefile'];
            f=open("demofile.jpg","wb")
            #print(x.readlines())
            #qrcode=ImageField(x)
            #bdp.profile_picture=x;
            #imwrite("saved.jpg",qrcode);
            
            f.writelines(x.readlines());
            #print("writeline = ",aa)
            f.close();
            data = decode(Image.open('demofile.jpg'));
            print(int(data[0][0]))
            x=bdp.objects.get(pk=int(data[0][0]))
            print(x);print(x.donor_address);print(x.contact);print(x.profile_picture)
            #print("request.files",x.readlines())
            context["found"]=True;context["name"]=x.donor_name;context["address"]=x.donor_address;context["contact"]=x.contact;context['picture']=x.profile_picture
            result={
        	'found':'true',
	        'name':x.donor_name,'address':x.donor_address,"contact":x.contact,"picture":x.profile_picture

	    }
            return render(request,'hospitalhome.html',context=context)
        else:
            
            x=bdp.objects.get(pk=8)
            
            #x=4
            print("user id  ",x)
            #print("post ",request.POST['bloodgroup'])
            print(request.FILES);
            x.blood_group='A+'
            x.blood_report=request.FILES['reportform']
            x.save()
       
    else:
        time.sleep(2)
        print("inside the else part")
    context["found"]=False   
    return render(request,'hospitalhome.html',context=context)

def validate_qrcode(request):
    if request.method=='POST':
        #if 'qrbutton' in list(request.POST.keys()):
            #print("qrbutton")
        print("request post ",request.POST)
        print("request files ",request.FILES)
		#image = request.GET.get('image', None)
        form=request.POST;
	#	print("form is ",request.FILES)
    data={
	'found':'true',
	'name':"nandan",'address':"manipal","contact":"909090900"

	}
    return JsonResponse(data)
