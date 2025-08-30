from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # <-- This saves the new user to the database
            login(request, user)  # Optional: log in the user immediately after registration
            return redirect("home")  # Replace "home" with your homepage URL name
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})
