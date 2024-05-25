from django.urls import path, re_path
from . import views

urlpatterns = [
    # Path converters
    # int: numbers
    # str: strings
    # path: whole urls/
    # slug: hyphen-and_underscores
    # UUID: Universally unique identifier
    path("account-login/", views.account_login, name="account-login"),
    path("account-logout/", views.account_logout, name="account-logout"),
]
