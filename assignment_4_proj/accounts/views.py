from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

def account_login(request):
    if request.method == "POST":
        login_value = request.POST.get("login_value", "")
        password = request.POST.get("password", "")

        print("login_value:", login_value)  # Debug: Print the login_value
        print("password:", password)  # Debug: Print the password

        User_model = get_user_model()
        user = User_model.objects.filter(username=login_value).first()
        print("user (by username):", user)  # Debug: Print the user object (if found by username)

        if not user:
            user = User_model.objects.filter(email=login_value).first()
            print("user (by email):", user)  # Debug: Print the user object (if found by email)

        if user:
            # Check if user is active
            if not user.is_active:
                print("User is not active.")
                messages.error(request, "This account is inactive.")
                return redirect("account-login")

            # Authenticate user
            authenticated_user = authenticate(request, username=user.username, password=password)
            print("authenticated user:", authenticated_user)  # Debug: Print the authenticated user object

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("management-index")

        messages.error(request, "Invalid username/email or password. Try again.")
        return redirect("account-login")

    else:
        context = {}
        return render(request, "accounts/accounts_login.html", context)

def account_logout(request):
    logout(request)
    return redirect('home')
