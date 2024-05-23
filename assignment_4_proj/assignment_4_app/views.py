from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from management.models import Project
from management.forms import ProjectForm
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, "assignment_4_app/index.html")

def project_details(request, slug):
    # try: 
        current_project = Project.objects.get(topic_num = slug)
 
        context = {
            "project": current_project
        }


        return render(request, "assignment_4_app/projectDetails.html", context)
    # except:
        # return HttpResponseNotFound("This link is not supported")

# http://127.0.0.1:8000/project-list
def project_list(request):
    try: 
        projects_list = Project.objects.all().order_by("topic_num")

        context = {
            "projects": projects_list,
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
    
def Search(request):
    # try:
        if request.method == "POST":
            searched = request.POST['searched']
            projects = Project.objects.filter(
                Q(title__icontains=searched) |
                Q(supervisor__username__icontains=searched) |
                Q(topic_num__icontains=searched)
                )

            context = {
                'searched': searched,
                'projects': projects,
            }
            return render(request, "assignment_4_app/search.html", context)
        else:
            return render(request, "assignment_4_app/search.html")
    # except:
        # return HttpResponseNotFound("This link is not supported")

