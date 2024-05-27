from django.contrib import admin

# Register your models here.
from .models import Project, ProjectChangeRequest


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'topic_num')
    ordering = ('topic_num',)
    search_fields = ('title', 'supervisor')

@admin.register(ProjectChangeRequest)
class ProjectChangeRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'topic_num')
    ordering = ('topic_num',)
    search_fields = ('title', 'supervisor')
