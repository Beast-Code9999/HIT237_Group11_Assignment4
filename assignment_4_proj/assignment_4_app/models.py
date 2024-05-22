from django.db import models

class Supervisor(models.Model):
    first_name = models.CharField("First name(s)", max_length=50, null=True)
    last_name = models.CharField("Last name", max_length=50, null=True)
    staff_id = models.CharField("Staff ID", max_length=20, null=True)
    email = models.EmailField(max_length = 254, null=True)

    def __str__(self):
        return self.staff_id + ": " + self.first_name + " " + self.last_name 


# Create your models here.
class Project(models.Model):
    supervisor = models.ForeignKey(Supervisor, null=True, on_delete=models.RESTRICT) # one to many relationship, one supervisor can have multiple Projects
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=200, null=True)
    topic_num = models.IntegerField("Topic number", null=True)
    location = models.CharField("location", max_length=100, null=True)
    research_areas = models.CharField("Fields of study", max_length=100, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title + ", topic Number: " + str(self.topic_num)

class Student(models.Model):
    first_name = models.CharField("First name(s)", max_length=50, null=True)
    last_name = models.CharField("Last name", max_length=50, null=True)
    student_id = models.CharField("Student ID", max_length=20, null=True)
    email = models.EmailField(max_length = 254, null=True)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.RESTRICT) # in case students does not  have a thesis project yet


    def __str__(self):
        return self.student_id + ": " + self.first_name + " " + self.last_name 
    
class StudentGroup(models.Model):
    name = models.CharField(max_length=100, null=True)
    members = models.ManyToManyField(Student, related_name='student_groups', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

