from django.contrib import admin

# Register your models here.
from .models import Project, ProjectDetail, Student, StudentGroup, Supervisor

admin.site.register(Project)
admin.site.register(ProjectDetail)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Supervisor)