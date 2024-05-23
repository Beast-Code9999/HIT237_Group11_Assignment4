from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Project
from .forms import ProjectForm
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "management/management_index.html")

def manage_project(request):
    return render(request, "management/management_project.html")

def add_project(request):
    try:
        submitted = False
        if request.method == "POST":
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/add-project?submitted=True")
            else: 
                return HttpResponse("Something is wrong with the code")

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
            return redirect("project-details", slug = current_project.topic_num)

        context = {
            "project": current_project,
            "form": form,
        }
        return render(request, "management/updateProject.html", context)
    except:
        HttpResponseNotFound("Something wrong with the link")

def delete_project(request, slug):
    current_project = Project.objects.get(topic_num = slug)
    current_project.delete()
    return redirect("management-project")
