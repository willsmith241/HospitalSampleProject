from django.urls import path
from .views import create_doctor,doctor_list,register_doctor,doctor_login
urlpatterns = [
    path('doctor_create/',create_doctor,name='doctor_create'),
    path('doctor_list/',doctor_list,name='doctor_list'),
    path('',register_doctor,name='doctor_register'),
    path('doctor_login',doctor_login,name='doctor_login'),
]