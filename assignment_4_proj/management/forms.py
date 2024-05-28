from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Project, RequestAdd, RequestUpdate


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


class RequestUpdateForm(ModelForm):
    class Meta:
        model = RequestUpdate
        
        fields = ('title', 'category', 'topic_num', 'location', 'research_areas', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class':'input'}),
            'topic_num': forms.NumberInput(attrs={'class': "inputNum"}),
            'category': CheckboxSelectMultiple(attrs={'class': "checkbox"}),  # Use the built-in CheckboxSelectMultiple widget
            'location': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            'research_areas': CheckboxSelectMultiple(attrs={'class': "checkbox"}),
            "description": forms.Textarea(attrs={'class':'textarea'}),
        }

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super(RequestUpdateForm, self).__init__(*args, **kwargs)

        if project:
            self.fields['title'].initial = project.title
            self.fields['description'].initial = project.description
            self.fields['categories'].initial = project.categories.all()
            self.fields['locations'].initial = project.locations.all()
            self.fields['research_areas'].initial = project.research_areas.all()
            self.fields['category'].initial = project.category.all()


