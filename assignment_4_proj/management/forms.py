from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Project, RequestAdd


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        
        fields = ('supervisor', 'title', 'category', 'topic_num', 'location', 'research_areas', 'description')

        widgets = {
            'supervisor': forms.Select(attrs={'class':'input'}),
            'title': forms.TextInput(attrs={'class':'input'}),
            'topic_num': forms.NumberInput(attrs={'class': "inputNum"}),
            'category': CheckboxSelectMultiple(attrs={'class': "checkbox"}),  # Use the built-in CheckboxSelectMultiple widget
            'location': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            'research_areas': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            "description": forms.Textarea(attrs={'class':'textarea'}),
        }

class SupervisorProjectForm(ModelForm):
    class Meta:
        model = Project
        
        fields = ('title', 'category', 'topic_num', 'location', 'research_areas', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class':'input'}),
            'topic_num': forms.NumberInput(attrs={'class': "inputNum"}),
            'category': CheckboxSelectMultiple(attrs={'class': "checkbox"}),  # Use the built-in CheckboxSelectMultiple widget
            'location': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            'research_areas': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            "description": forms.Textarea(attrs={'class':'textarea'}),
        }

class RequestAddForm(ModelForm):
    class Meta:
        model = RequestAdd
        
        fields = ('title', 'category', 'topic_num', 'location', 'research_areas', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class':'input'}),
            'topic_num': forms.NumberInput(attrs={'class': "inputNum"}),
            'category': CheckboxSelectMultiple(attrs={'class': "checkbox"}),  # Use the built-in CheckboxSelectMultiple widget
            'location': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            'research_areas': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            "description": forms.Textarea(attrs={'class':'textarea'}),
        }



