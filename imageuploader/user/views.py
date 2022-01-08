from django.shortcuts import render

from.forms import ImageForm
from .models import Image
from django.shortcuts import render,redirect, HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout,hashers
from django.contrib.auth.models import User, Group,auth


# Create your views here.
def home(request):
  return render(request,'index.html')
def signup(request):
  return render(request,'sign.html')

def photo(request):
  if request.user.is_authenticated:
    
      
    if request.method=='POST':
      form=ImageForm(request.POST,request.FILES)
      if form.is_valid():
        form.save()
        messages.success(request,'Image Successfully Uploaded')
  
  else:
    return redirect("/login/")
    
    
  form=ImageForm()
  d= Image.objects.all() 
  name=request.user
  return render(request,'photo.html',{'dd':d,'form':form,'name':name})



def login(request):
  if request.user.is_authenticated:
    return redirect("/photo/")
    
  else:

    if request.method=='POST':
      username=request.POST['username']
      password1=request.POST['password1']
      user = auth.authenticate(username=username ,password=password1)

      if user is not None:
        auth.login(request,user)
        return redirect("/photo/")
      else:
        messages.info(request,'Username and Password not Match')
        return render(request,'login.html')
  

  return render(request,'login.html')


def user_logout(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request,'Logout Succesfully')
    return redirect('/login/')
