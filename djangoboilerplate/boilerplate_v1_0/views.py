from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from boilerplate_v1_0.forms import CustomerCreationForm


def dashboard(request):
    return render(request=request, template_name="./users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomerCreationForm}
        )
    elif request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
