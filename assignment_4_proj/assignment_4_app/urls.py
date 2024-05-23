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
    path("search/", views.Search, name="search"),
    re_path("add-project/", views.add_project, name="add-project"),
    re_path(r"^update-project/(?P<slug>\d+)$", views.update_project, name="update-project"),
    re_path(r"^delete-project/(?P<slug>\d+)$", views.delete_project, name="delete-project"),

]
