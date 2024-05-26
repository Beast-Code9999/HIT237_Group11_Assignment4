from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

def account_login(request):
    if request.method == "POST":
        login_value = request.POST.get("login_value", "")
        password = request.POST.get("password", "")
        
        # print("login_value:", login_value)
        # print("password:", password)

        # Get the User model
        User_model = get_user_model()
        
        # Try to get the user by username
        user = User_model.objects.filter(username=login_value).first()
        
        # If user not found by username, try to find by email
        if not user:
            user = User_model.objects.filter(email=login_value).first()
        
        # If user is found, authenticate and login
        if user:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("management-index")
        
        # If user is not found or authentication fails, display error message
        messages.error(request, "Invalid username/email or password. Try again.")
        return redirect("account-login")
    else:
        context = {}
        return render(request, "accounts/accounts_login.html", context)
    

def account_logout(request):
    logout(request)
    return redirect('home')
                   