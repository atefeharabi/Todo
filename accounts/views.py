from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterationForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'Registered successfully', 'success')
            return redirect('home')
    else:
        form = UserRegisterationForm()
    return render(request, 'register.html', {'form': form})