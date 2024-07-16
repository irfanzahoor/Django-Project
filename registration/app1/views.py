from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'signup.html', {'error': "Your password and confirm password are not the same!"})

        if User.objects.filter(username=uname).exists():
            return render(request, 'signup.html', {'error': "Username already exists!"})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': "Email already exists!"})

        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()
        return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')  # Ensure the field name matches your form
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': "Username or Password is incorrect!"})

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
