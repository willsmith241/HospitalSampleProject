from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AdminLoginForm
from doctor_app.models import RegisterDoctor,DoctorCreate
# Create your views here.
from patient_app.models import UserProfile,BookAppointment
from django.shortcuts import render, redirect, get_object_or_404

def booking_list(request):
    bookings = BookAppointment.objects.all()

    return render(request,'admin/appointment_list.html',{'bookings':bookings})

def delete_appointment(request,id):
    appointment = BookAppointment.objects.get(id=id)
    if request.method == "POST":
        appointment.delete()

        return redirect('dashboard')
    return render(request,'admin/appointment_delete.html')
def admin_dashboard(request):
    total_doctors = DoctorCreate.objects.count()  # Count total doctors
    total_patients = UserProfile.objects.count()
    total_bookings = BookAppointment.objects.count()# Count total patients

    return render(request, 'admin/dashboard.html', {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_bookings':total_bookings,
    })

def home(request):

    return render(request,'home.html')


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('dashboard')  # Replace with your admin dashboard URL
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AdminLoginForm()

    return render(request, 'admin/login.html', {'form': form})

def doctor_list(request):
   doctors = DoctorCreate.objects.all()

   return render(request,'admin/doctor_list.html',{'doctors':doctors})

def patient_list(request):
    patients = UserProfile.objects.all()

    return render(request,'admin/patient_list.html',{'patients':patients})

def doc_register_list(request):
    doctors_page = DoctorCreate.objects.all()

    return render(request,'admin/doctor_register_list.html')


def delete_doctor(request,doc_id):

    doctor=DoctorCreate.objects.get(id=doc_id)

    if request.method=="POST":

        doctor.delete()

        return redirect('dashboard')

    return render(request,'admin/doctor_delete.html',{'doctor':doctor})

def patient_delete(request,id):
    patient = UserProfile.objects.get(id=id)

    if request.method == "POST":
        patient.delete()

        return redirect('dashboard')

    return render(request,'admin/patient_delete.html',{'patient':patient})

