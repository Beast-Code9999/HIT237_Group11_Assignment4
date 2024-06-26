from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    supervisor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    category = models.ManyToManyField("Category", blank=True)
    topic_num = models.PositiveIntegerField("Topic number", null=True, unique=True)
    location = models.ManyToManyField("Location", blank=True)
    research_areas = models.ManyToManyField("ResearchArea", blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title + ", topic Number: " + str(self.topic_num)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
               
class ResearchArea(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class RequestAdd(models.Model):
    supervisor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    category = models.ManyToManyField("Category", blank=True)
    topic_num = models.PositiveIntegerField("Topic number", null=True, unique=True)
    location = models.ManyToManyField("Location", blank=True)
    research_areas = models.ManyToManyField("ResearchArea", blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("approved", "Approved"), {"rejected", "Rejected"}], default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title + ", Status: " + str(self.status)
    
class RequestUpdate(models.Model):
    supervisor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    category = models.ManyToManyField("Category", blank=True)
    topic_num = models.PositiveIntegerField("Topic number", null=True, unique=True)
    location = models.ManyToManyField("Location", blank=True)
    research_areas = models.ManyToManyField("ResearchArea", blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("approved", "Approved"), {"rejected", "Rejected"}], default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title + ", Status: " + str(self.status)



# class RequestDelete():
#     pass


