from django.urls import path, re_path
from . import views

urlpatterns = [
    # Path converters
    # int: numbers
    # str: strings
    # path: whole urls/
    # slug: hyphen-and_underscores
    # UUID: Universally unique identifier
    path("", views.home, name="home"),
    # http://127.0.0.1:8000/project-list
    path("project-list/", views.project_list, name="project-list"),
    # http://127.0.0.1:8000/project-details/<identifier>
    path("project-details/<slug:slug>/", views.project_details, name="project-details"), # project-details/proj1 etc... using path transformer other e.g. is int or str
    # http://127.0.0.1:8000/about
    path("about-us/", views.about, name="about"),   
    re_path("manage-project/", views.manage_project, name="manage-project"),
]
