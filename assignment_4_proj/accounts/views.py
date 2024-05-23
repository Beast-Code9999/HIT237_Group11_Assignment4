from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def account_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect("manage-project")
        else:
            messages.success(request, {"There was an error. Try again"})
            return redirect("account-login")
    else:

        context = {

        }

        return render(request, "accounts/accounts_login.html", context)