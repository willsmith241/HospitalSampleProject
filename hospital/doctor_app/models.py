from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class DoctorCreate(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_img = models.ImageField(upload_to='media/')
    doc_phone = models.IntegerField()
    license_number = models.IntegerField()

    def __str__(self):
        return self.doc_name

class RegisterDoctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    hospital_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    hospital_name = models.CharField(max_length=200)
    # Add any other fields needed for your doctor

    def __str__(self):
        return self.username

