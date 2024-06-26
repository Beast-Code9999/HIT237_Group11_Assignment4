from django.urls import path, re_path
from . import views

urlpatterns = [
    # Path converters
    # int: numbers
    # str: strings
    # path: whole urls/
    # slug: hyphen-and_underscores
    # UUID: Universally unique identifier
    path("", views.index, name="management-index"),
    path("projects/", views.manage_project, name="manage-project"),
    re_path("add-project/?", views.add_project, name="add-project"),
    re_path(r"^update-project/(?P<slug>\d+)$", views.update_project, name="update-project"),
    re_path(r"^delete-project/(?P<slug>\d+)$", views.delete_project, name="delete-project"),
    path("project-csv/", views.project_csv, name="project-csv"),
    path("project-pendings/", views.project_request_list, name="project-pendings"),
    path("project-pendings/approve/<slug>", views.approve_project_request, name="approve-project-request"),
    path("project-pendings/reject/<slug>", views.reject_project_request, name="reject-project-request"),
    path("project-pendings/update/<slug>", views.update_pending_project, name="update-pending-project"),
    path("project-pendings/delete/<slug>", views.delete_pending_request, name="delete-pending-project"),

]
