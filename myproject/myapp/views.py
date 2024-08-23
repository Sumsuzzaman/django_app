from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World")

def homepage(request):
    page = {
        "title": "Homepage",
    }
    return render(request, "index.html", page)

def about(request):
    return render(request, "about.html")

def contact(request):
    hq = "d"
    email = "bXuRy@example.com"
    socialprofiles = {
        "github: https://github.com",
        "linkedin: https://linkedin.com",
        "twitter: https://twitter.com",
    }

    return render(request, "contact.html", {"email": email, "socialprofiles": socialprofiles, "hq": hq})  

def experiment(request, person= None):    
    if person == None:
        person = "Guest"
    return render(request, "experiment.html",{"data": person})