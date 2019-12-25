from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomSignUpForm


def register(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('fst_name')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('welcome')
    else:
        form = CustomSignUpForm()
    return render(request, 'register.html', {'form': form})


def welcome(request):
    return render(request, 'welcome.html')
