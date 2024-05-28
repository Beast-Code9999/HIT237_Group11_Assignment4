from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Project, ProjectChangeRequest
from .forms import ProjectForm, ProjectChangeRequest, SupervisorProjectForm
from django.db.models import Q
import csv
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


# Create your views here.
def index(request):
    return render(request, "management/management_index.html")

@login_required
@user_passes_test(lambda user: user.user_type in ['supervisor', 'unit_coordinator'])
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
            if request.user.user_type in ["unit_coordinator"]: # check if user is unit_coordinator, if so, save ProjectForm
                form = ProjectForm(request.POST)
                if form.is_valid():
                    form.save()
                    submitted = True  # Set submitted to True after successful form submission
                    return HttpResponseRedirect(reverse('add-project') + '?submitted=True')
                else: 
                    return HttpResponse("Project already exist")
            else: # else save restricted form (no supervisor field)
                form = SupervisorProjectForm(request.POST)
                if form.is_valid():
                    project = form.save(commit=False)
                    project.supervisor = request.user
                    project.save()
                    form.save_m2m()  # Ensure many-to-many relationships are saved
                    return HttpResponseRedirect(reverse('add-project') + '?submitted=True')
                else: 
                    return HttpResponse("Project already exist")
        else:
            if request.user.user_type in ["unit_coordinator"]:
                form = ProjectForm
            else:
                form = SupervisorProjectForm

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

        if request.user.user_type in ["unit_coordinator"]:
            form = ProjectForm(request.POST or None, instance=current_project)
        else:
            form = SupervisorProjectForm(request.POST or None, instance=current_project)

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