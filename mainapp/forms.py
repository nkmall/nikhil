from django import forms
# from django.contrib.auth.models import User
from . models import User,Student
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class registrationForm(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2=forms.CharField(label="confirm Password",widget=forms.PasswordInput(attrs={"class": "form-control"}))
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('G', 'Gay'),
        ('L', 'Lesbian')
    )
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES, widget=forms.Select(attrs={"class": "form-select"}))
    class Meta(UserCreationForm):
        model=User
        fields=["username","email","first_name","last_name","mobile_no","gender"]
        widgets={
            "username":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class": "form-control"}),
            "first_name":forms.TextInput(attrs={"class": "form-control"}),
            "last_name":forms.TextInput(attrs={"class": "form-control"}),
            "mobile_no":forms.TextInput(attrs={"class": "form-control"}),
        }       

class Userloginform(AuthenticationForm):
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={"class": "form-control"}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class": "form-control"}))


class studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class": "form-control"}),
            "roll":forms.NumberInput(attrs={"class": "form-control"}),
            "class_name":forms.TextInput(attrs={"class": "form-control"})
        } 
