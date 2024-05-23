# from django import forms
# from django.forms import ModelForm
# from .models import Project

# # Create a form for Project
# class ProjectForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ('supervisor', 'title', 'category', 'topic_num', 'location', 'research_areas', 'description')
#         labels = {
#             'supervisor': '',
#             'title': '',
#             'category': '',
#             'topic_num': '',
#             'location': '',
#             'research_areas': '',
#             'description': '',
#         }

#         widgets = {
#             'supervisor': forms.Select(attrs={'class': 'input__text', 'placeholder': "Supervisor"}),
#             'title': forms.TextInput(attrs={'class': 'input__text', 'placeholder': "Title"}),
#             'category': forms.TextInput(attrs={'class': 'input__text', 'placeholder': "Category"}),
#             'topic_num': forms.NumberInput(attrs={'class': 'input__text', 'placeholder': "Topic Number"}),
#             'location': forms.TextInput(attrs={'class': 'input__text', 'placeholder': "Location"}),
#             'research_areas': forms.TextInput(attrs={'class': 'input__text', 'placeholder': "Fields of study"}),
#             'description': forms.Textarea(attrs={'class': 'input__textarea', 'placeholder': "Description"}),
#         } 