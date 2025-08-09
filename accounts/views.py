# accounts/views.py
import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import TempEmail, UserDetails
from django.contrib.auth.hashers import make_password

def email_page(request):
    if request.method == "POST":
        email = request.POST['email']
        otp = str(random.randint(100000, 999999))
        TempEmail.objects.update_or_create(email=email, defaults={'otp': otp, 'verified': False})
        send_mail(
            'Your OTP Code',
            f'Your OTP is {otp}',
            'your_email@gmail.com',
            [email],
            fail_silently=False,
        )
        request.session['email'] = email
        return redirect('verify_otp')
    return render(request, 'accounts/email.html')

def verify_otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        email = request.session.get('email')
        temp = TempEmail.objects.get(email=email)
        if temp.otp == otp:
            temp.verified = True
            temp.save()
            return redirect('register_details')
        else:
            return render(request, 'accounts/verify_otp.html', {'error': 'Invalid OTP'})
    return render(request, 'accounts/verify_otp.html')

def register_details(request):
    email = request.session.get('email')
    temp = TempEmail.objects.get(email=email)
    if not temp.verified:
        return redirect('email_page')

    if request.method == "POST":
        username = request.POST['username']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        UserDetails.objects.create(email=email, username=username, phone=phone, password=password)
        return redirect('login')
    return render(request, 'accounts/register_details.html')

def login_view(request):
    return render(request, 'accounts/login.html')
