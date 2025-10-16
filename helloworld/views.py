# helloworld-chat/helloworld/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AddContactForm


def home(request):
    if request.method == "GET":
        form = AddContactForm()
    elif request.method == "POST":
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print("----> Problem while adding the user from Pop-up!")
    else:
        print("----> error in the add_user pop up form!")

    return render(request, "helloworld/home.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print("----> signup_form failed!")

    elif request.method == "GET":
        form = UserCreationForm()

    else:
        print("----> error in the Signup view")

    return render(request, "registration/signup.html", {"form": form})
