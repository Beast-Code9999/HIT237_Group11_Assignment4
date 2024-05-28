from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Project, ProjectChangeRequest, RequestAdd
from .forms import ProjectForm, ProjectChangeRequest, SupervisorProjectForm, RequestAddForm
from django.db.models import Q
import csv
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils import timezone


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
                form = RequestAddForm(request.POST)
                if form.is_valid():
                    project = form.save(commit=False)  # Save the form without committing to the database
                    project.supervisor = request.user  # Set the supervisor field to the current user
                    project.save()  # Save the main instance to the database
                    form.save_m2m()  # Save the many-to-many relationships
                    submitted = True  # Set submitted to True after successful form submission
                    return HttpResponseRedirect(reverse('add-project') + '?submitted=True')
                else: 
                    return HttpResponse("Project already exist")
        else:
            if request.user.user_type in ["unit_coordinator"]:
                form = ProjectForm
            else:
                form = RequestAddForm

            if 'submitted' in request.GET:
                submitted = True

            context = {
                "form": form,
                "submitted": submitted,
            }
            return render(request, "management/addProject.html", context)
    except:
        return HttpResponseNotFound("This link is not supported")
    
@login_required
@user_passes_test(lambda user: user.user_type in ['unit_coordinator'])
def approve_project_request(request, slug):
    project_request = get_object_or_404(RequestAdd, topic_num=slug)
    if request.method == "POST":
        project_request.status = "Approved"
        project_request.approved_at = timezone.now()
        project_request.save()

        # Create a new Project from the approved request
        project = Project.objects.create(
            supervisor=project_request.supervisor,
            title=project_request.title,
            topic_num=project_request.topic_num,
            description=project_request.description
        )
        project.category.set(project_request.category.all())
        project.location.set(project_request.location.all())
        project.research_areas.set(project_request.research_areas.all())
        project.save()

        project_request.delete() # currently saved project_request is immediately deleted, but this can be stored elsewhere in the future instead of being deleted right away

        return redirect('project-pendings')
    else: 
        context = {
            "project_request": project_request
        }

        return render(request, "management/management_approve_project.html", context)

@login_required
@user_passes_test(lambda user: user.user_type in ['unit_coordinator'])
def reject_project_request(request, slug):
    project_request = get_object_or_404(Project, topic_num=slug)

@login_required
@user_passes_test(lambda user: user.user_type in ['supervisor','unit_coordinator'])
def project_request_list(request):
    project_requests = RequestAdd.objects.filter(status="pending")

    context = {
        "project_requests": project_requests
    }
    
    return render(request, "management/management_project_pendings.html", context)




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