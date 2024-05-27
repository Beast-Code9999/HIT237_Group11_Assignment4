from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from management.models import Project, ProjectChangeRequest

class Command(BaseCommand):
    help = "Class to create groups for users"

    def handle(self, *args, **kwargs):
        groups = ["unit_coordinator", "supervisor", "student"]
        for group in groups:
            Group.objects.get_or_create(name=group)

            # Create groups and permissions
            if group == "unit_coordinator":
                permissions = [
                    'add_project',
                    'change_project',
                    'delete_project',
                    'view_project',
                    'add_projectchangerequest',
                    'change_projectchangerequest',
                    'delete_projectchangerequest',
                    'view_projectchangerequest'
                ]
            elif group == "supervisor":
                permissions = [
                    'add_projectchangerequest',
                    'change_projectchangerequest',
                    'delete_projectchangerequest',
                    'view_projectchangerequest'
                ]
            elif group == "student":
                permissions = ['view_project']

            # after defining permission array, loop thorugh array and assign permissions to the group
            for codename in permissions:
                if codename.startswith('project'):
                    content_type = ContentType.objects.get_for_model(Project)
                elif codename.startswith('projectchangerequest'):
                    content_type = ContentType.objects.get_for_model(ProjectChangeRequest)
                else:
                    # in case the content type cannot be found
                    self.stderr.write(f"Content type not found for permission '{codename}'. Skipping permission assignment.")
                    continue

                
                permission = Permission.objects.get(content_type=content_type, codename=codename)
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS("Grouprs have been created!"))
        
print("Content type for Project: ", ContentType.objects.get_for_model(Project))
print("Content type for ProjectChangeRequest: ", ContentType.objects.get_for_model(ProjectChangeRequest))