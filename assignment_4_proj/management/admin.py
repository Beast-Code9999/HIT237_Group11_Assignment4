from django.contrib import admin

# Register your models here.
from .models import Project, ProjectChangeRequest, Category, Location, ResearchArea


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


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(ResearchArea)