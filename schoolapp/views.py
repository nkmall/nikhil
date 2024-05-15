from django.shortcuts import render,HttpResponseRedirect
from mainapp.forms import studentform
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"school.html")

@login_required
def dashboard(request):
    fm=studentform
    return render(request,"dashboard.html",{"form":fm})