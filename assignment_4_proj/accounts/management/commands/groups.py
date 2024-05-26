from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Class to create groups for users"

    def handle(self, *args, **kwargs):
        groups = ["unit_coordinator", "supervisor", "student"]
        for group in groups:
            Group.objects.get_or_create(name=group)
        self.stdout.write(self.style.SUCCESS("Grouprs have been created!"))