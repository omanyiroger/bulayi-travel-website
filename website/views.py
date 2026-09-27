from django.shortcuts import render, redirect
from .models import Enquiry


def home(request):
    submitted = False

    if request.method == "POST":
        Enquiry.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            service=request.POST.get("service"),
            destination=request.POST.get("destination"),
            travel_date=request.POST.get("travel_date") or None,
            message=request.POST.get("message"),
        )

        submitted = True

    return render(request, "home.html", {"submitted": submitted})


def dubai(request):
    return render(request, "destinations/dubai.html")

def zanzibar(request):
    return render(request, "destinations/zanzibar.html")

def paris(request):
    return render(request, "destinations/paris.html")

def guangzhou(request):
    return render(request, "destinations/guangzhou.html")


def robots(request):
    return render(request, "robots.txt", content_type="text/plain")


def destinations(request):
    return render(request, "destinations.html")


def nairobi(request):
    return render(request, "destinations/nairobi.html")

def eldoret(request):
    return render(request, "destinations/eldoret.html")

def mombasa(request):
    return render(request, "destinations/mombasa.html")


def kisumu(request):
    return render(request, "destinations/kisumu.html")

def nakuru(request):
    return render(request, "destinations/nakuru.html")
