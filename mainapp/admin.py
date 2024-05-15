from django.contrib import admin
from . models import Student,User

admin.site.register(User)

@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display =["id", "name","class_name","roll"]
