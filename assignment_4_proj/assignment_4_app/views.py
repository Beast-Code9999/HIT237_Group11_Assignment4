from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Project

# Create your views here.
def home(request):
    return render(request, "assignment_4_app/index.html")

def project_details(request, slug):
    try: 
        return render(request, "assignment_4_app/projectDetails.html")
    except:
        return HttpResponseNotFound("This link is not supported")

# http://127.0.0.1:8000/project-list
def project_list(request):
    try: 
        projects_list = Project.objects.all()

        context = {
            "projects": projects_list
        }
        return render(request, "assignment_4_app/projectList.html", context)
    except:     
        return HttpResponseNotFound("This link is not supported")


# http://127.0.0.1:8000/about
def about(request):
    try:
        return render(request, "assignment_4_app/about.html")
    except:
        return HttpResponseNotFound("This link is not supported")
