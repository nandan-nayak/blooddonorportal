from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .forms import UserLoginForm
from .forms1 import SignUpForm
def donorlogin(request):
    context=dict()
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        #print("donor views ",dir(request.user.user2.blooddonor))
        login(request, user)
        #if next:
        #   return redirect(next)
        return redirect('donorhome')
    context['form']= form
    if request.method=='POST':
        print("POST method")
        form1=SignUpForm(request.POST,request.FILES) 
        #form2=FileUpload(request.FILES)
        #print(dir(form1.save()))
        #print("form1 ===",form1.is_valid())
        if form1.is_valid() :
            
            user=form1.save(file=request.FILES['profile_picture']) 
            #print(user.blooddonorprofile.)
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
            login(request, user)
            #user=authenticate(user=user.username,password=raw_password)
            #print("dir====",dir(user))
            #login(request,user)
            return redirect('donorhome')
        
    else:
        form1=SignUpForm()
        #form2=FileUpload()
    context['form1']=form1
    #context['form2']=form2
    #return render(request,'loginpage.html',context)
    return render(request,'loginpagedonor.html',context)
def donorhome(request):
    return render(request,'donorhome.html')