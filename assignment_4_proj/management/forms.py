from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Project, ProjectChangeRequest


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('supervisor', 'title', 'category', 'topic_num', 'location', 'research_areas', 'description')
        widgets = {
            'category': CheckboxSelectMultiple(),  # Use the built-in CheckboxSelectMultiple widget
        }

class ProjectChangeRequestForm(ModelForm):
    class Meta:
        model = ProjectChangeRequest
        fields = ["project", "title", "category", "topic_num", "location", "research_areas", "description"]
        widgets = {
            'category': CheckboxSelectMultiple(),  # Use the built-in CheckboxSelectMultiple widget
        }