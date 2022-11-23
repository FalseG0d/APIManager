from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def scrape(request):
    profile = { }

    if request.method == "POST":
        profile = {
            "name": request.POST.get('name')
        }

    return render(request, "test.html", profile)