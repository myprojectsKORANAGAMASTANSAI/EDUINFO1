from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import CustomUser  # Ensure CustomUser extends AbstractUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None and hasattr(user, 'role') and user.role == role:
            login(request, user)
            if user.role == 'Admin':
                return redirect('admin_dashboard')
            elif user.role == 'Teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'Student':
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username, password, or role.')
    
    return render(request, 'login.html')

def authentication(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        # Securely create the user
        user = CustomUser.objects.create_user(username=username, password=password, role=role)
        messages.success(request, 'User created successfully.')
        return redirect('login')
        
    return render(request, 'signup.html')

@login_required
def admin(request):
    if request.user.role != 'Admin':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('login')
    return render(request, 'admin.html')

@login_required
def teacher(request):
    if request.user.role != 'Teacher':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('login')
    return render(request, 'teacher.html')

@login_required
def student(request):
    if request.user.role != 'Student':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('login')
    return render(request, 'student.html')

@login_required
def admission(request):
    return render(request, 'admission.html')

@login_required
def school_of_computings(request):
    return render(request, 'computing_admission/base_computing.html')

@login_required
def admission_aiml(request):
    return render(request, 'computing_admission/AIML.html')
@login_required
def admission_Software_Engineering(request):
    return render(request, 'computing_admission/Software_Engineering.html')


@login_required
def admiss_Data_Sciences(request):
    return render(request, 'computing_admission/Data_Science.html')

@login_required
def admission_cybersecurity(request):
    return render(request, 'computing_admission/cybersecurity.html')

@login_required
def admision_block_techonogly(request):
    return render(request,"computing_admission/block_techonogly.html")

@login_required
def admission_internet_of_things(request):
    return render(request,"computing_admission/IOT.html")
@login_required
def admission_cloud_computing(request):
    return render(request,"computing_admission/cloud_computing.html")

@login_required
def admission_computer_networks(request):
    return render(request,"computing_admission/computer_networks.html")

