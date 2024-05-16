from django.db import models

# Create your models here.
class Projects(models.Model):
    supvervisor = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

class ProjectDetails(models.Model):
    pass

class Students(models.Model):
    pass

class Supervisors(models.Model):
    pass
