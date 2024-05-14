from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # http://127.0.0.1:8000/project-list
    path("project-list/", views.project_list, name="project-list"),
    # http://127.0.0.1:8000/project-details/<identifier>
    path("project-details/<slug:slug>/", views.project_details, name="project-details"), # project-details/proj1 etc... using path transformer other e.g. is int or str
    # http://127.0.0.1:8000/about
    path("about-us/", views.about, name="about"),   
]
