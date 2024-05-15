from django.urls import path
from mainapp import views
urlpatterns = [
    path('',views.index),
    path("registration/",views.registrations),
    path("login/",views.userlogin,name="login"),
    path("logout/",views.userlogout)
]
