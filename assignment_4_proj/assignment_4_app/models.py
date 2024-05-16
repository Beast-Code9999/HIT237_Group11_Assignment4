from django.db import models

# Create your models here.
class Project(models.Model):
    supvervisor = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

class ProjectDetail(models.Model):
    pass

class Student(models.Model):
    pass

class StudentGroup(models.Model):
    pass

class Supervisor(models.Model):
    pass
