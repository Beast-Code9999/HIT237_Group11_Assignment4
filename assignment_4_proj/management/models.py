from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    supervisor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # one to many relationship, one supervisor can have multiple Projects
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=200, null=True)
    topic_num = models.PositiveIntegerField("Topic number", null=True, unique=True)
    location = models.CharField("location", max_length=100, null=True)
    research_areas = models.CharField("Fields of study", max_length=100, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title + ", topic Number: " + str(self.topic_num)
    