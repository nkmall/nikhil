from django.urls import path
from schoolapp import views
urlpatterns = [
    path('school/',views.home),
    path('dashboard/',views.dashboard),

]
