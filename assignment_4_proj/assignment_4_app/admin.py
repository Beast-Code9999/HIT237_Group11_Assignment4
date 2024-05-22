from django.contrib import admin

# Register your models here.
from .models import Project, Student,StudentGroup, Supervisor

# admin.site.register(Project)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Supervisor)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'topic_num')
    ordering = ('topic_num',)
    search_fields = ('title', 'supervisor')