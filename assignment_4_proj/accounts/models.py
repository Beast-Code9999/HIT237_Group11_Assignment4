from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('unit_coordinator', 'Unit Coordinator'),
        ('supervisor', 'Supervisor'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')

    # Specify a different related_name for the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set',
        related_query_name='user',
    )

    # Specify a different related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='user',
    )


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='supervisor')

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='student')

    def __str__(self):
        return self.user.username