from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "WebProjectApp/home.html")

def shop(request):
    return render(request, "WebProjectApp/shop.html")
