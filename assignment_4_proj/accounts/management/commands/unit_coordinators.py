# create unit_coordinators (same logic as supervisors but different group name and user_type)

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils import timezone

class Command(BaseCommand):
    help = "Create unit coordinator users"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Ensure the unit coordinator group exists
        unit_coordinator_group, created = Group.objects.get_or_create(name='unit_coordinator')

        # An arrya of unit coordinators objects, where we define our unit coordinators
        unit_coordinators_data = [
            {
                'username': 'unit_coordinator',
                'password': 'password',
                'first_name': 'group',
                'last_name': 'eleven',
                'email': 'unitcoordinator@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'unit_coordinator'
            },
            {
                'username': 'yakub_unit_coordinator',
                'password': 'yakubpassword',
                'first_name': 'Yakub',
                'last_name': 'Sebastian',
                'email': 'yakubunitcoordinator@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'unit_coordinator'
            },

            # In the future if we want to create more unit coordinators, we just add these objects here
        ]

        for coordinator_data in unit_coordinators_data:
            user, created = User.objects.get_or_create(
                username=coordinator_data['username'],
                defaults={
                    'first_name': coordinator_data['first_name'],
                    'last_name': coordinator_data['last_name'],
                    'email': coordinator_data['email'],
                    'date_joined': coordinator_data['date_joined'],
                    'user_type': coordinator_data['user_type']
                }
            )
            if created:
                user.set_password(coordinator_data['password'])
                user.save()
                user.groups.add(unit_coordinator_group)
                self.stdout.write(self.style.SUCCESS(f"Unit Coordinator {coordinator_data['username']} created successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Unit Coordinator {coordinator_data['username']} already exists"))

        self.stdout.write(self.style.SUCCESS('Finished creating unit coordinator users'))
