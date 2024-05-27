from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Project, ProjectChangeRequest
from .forms import ProjectForm, ProjectChangeRequest
from django.db.models import Q
import csv
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    return render(request, "management/management_index.html")

def manage_project(request):
    projects_list = Project.objects.all().order_by("topic_num")

    context = {
        "projects": projects_list
    }

    return render(request, "management/management_project.html", context)

def add_project(request):
    try:
        submitted = False
        if request.method == "POST":
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('add-project') + '?submitted=True')
            else: 
                return HttpResponse("Project already exist")

        else:
            form = ProjectForm()

            if 'submitted' in request.GET:
                submitted = True
            context = {
                "form": form,
                "submitted": submitted,
            }
            return render(request, "management/addProject.html", context)
    except:
        return HttpResponseNotFound("This link is not supported")

def update_project(request, slug):
    try:
        current_project = get_object_or_404(Project, topic_num=slug)

        form = ProjectForm(request.POST or None, instance=current_project)

        if form.is_valid():
            form.save()
            return redirect("manage-project")

        context = {
            "project": current_project,
            "form": form,
        }
        return render(request, "management/updateProject.html", context)
    except:
        return HttpResponseNotFound("Something wrong with the link")

def delete_project(request, slug):
    current_project = Project.objects.get(topic_num = slug)
    current_project.delete()
    return redirect("manage-project")


def project_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["content-Disposition"] = "attachment; filename=projects.csv"

    write = csv.writer(response)

    projects = Project.objects.all()

    write.writerow(['Supervisor', 'Title', 'Category', 'Topic Number', 'Location', 'Research Areas', 'Description'])

    for project in projects:
        write.writerow([project.supervisor, project.title, project.category, project.topic_num, project.location, project.research_areas, project.description])

    return response