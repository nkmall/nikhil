from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('G', 'Gay'),
    ('L', 'Lesbian')
)
class User(AbstractUser):
    address=models.CharField(max_length=100,verbose_name="address line1")
    mobile_no=models.IntegerField(null=True,verbose_name="pnone no")
    gender=models.CharField(max_length=2,choices=GENDER_CHOICES)

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField(null=True)
    class_name=models.CharField(max_length=50)

    def __str__(self):
        return self.name,self.roll,self.class_name