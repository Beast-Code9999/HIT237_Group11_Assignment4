from django.contrib import admin

# Register your models here.
from .models import Project, Category, Location, ResearchArea, RequestAdd, RequestUpdate


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'topic_num')
    ordering = ('topic_num',)
    search_fields = ('title', 'supervisor')


@admin.register(RequestAdd)
class RequestAddAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'topic_num')
    ordering = ('topic_num',)
    search_fields = ('title', 'supervisor')

@admin.register(RequestUpdate)
class RequestUpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'topic_num')
    ordering = ('topic_num',)
    search_fields = ('title', 'supervisor')

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(ResearchArea)