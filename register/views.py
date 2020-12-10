from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")

    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
