from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully. Please login.') 
                form.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form' : form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    messages.success(request, 'Successfully logged in.')
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return redirect('profile')

def user_logout(request):
    messages.success(request, 'Successfully logged out.')
    logout(request)
    return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Profile updated successfully.')
                form.save()
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, 'profile.html', {'form':form})
    else:
        messages.success(request, 'Please login first.')
        return redirect('login')
    
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request, 'Password changed successfully.')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form':form})
    else:
        messages.success(request, 'You must login first.')
        return redirect('login')
    
def set_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request, 'Password set successfully.')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'changepass.html', {'form':form})
    else:
        messages.success(request, 'You must login first.')
        return redirect('login')
    
