from django.shortcuts import render

# Create your views here.
def home():
    return render(request, "management/home.html")