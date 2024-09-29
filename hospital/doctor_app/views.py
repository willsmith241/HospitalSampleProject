from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .forms import CreateDoctorForm
from .models import DoctorCreate,RegisterDoctor
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login



# Create your views here.

def create_doctor(request):
    if request.method =='POST':

        form = CreateDoctorForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = CreateDoctorForm()
    return render(request,'doctor/create_doctor.html',{'form':form})

def doctor_list(request):
    doctors = DoctorCreate.objects.all()


    return render(request,'doctor/doctor_list.html',{'doctors':doctors})



def register_doctor(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()
            login(request, user)
            return redirect('doctor_login')  # Update as needed
    else:
        form = CustomUserCreationForm()
    return render(request, 'doctor/doctor_register.html', {'form': form})


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('booking_list')  # Update as needed
    return render(request, 'doctor/doctor_login.html')











