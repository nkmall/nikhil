from django.shortcuts import render,HttpResponseRedirect
from . forms import registrationForm,Userloginform
from django.contrib.auth import authenticate,logout,login
# from django.contrib.auth import logout,login

def index(request):
    return render(request, "index.html")

def registrations(request):
    if request.method=="POST":
        fm=registrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/login/")
    fm=registrationForm()
    return render(request, "home.html",{"form":fm})


def userlogin(request):
    if request.method=="POST":
        fm=Userloginform(request=request,data=request.POST)
        if fm.is_valid():
            un=fm.cleaned_data.get("username")
            ps=fm.cleaned_data.get("password")
            user=authenticate(username=un,password=ps)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/school/dashboard/")
    fm=Userloginform()
    return render(request,"loginform.html",{"form":fm})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/login/")