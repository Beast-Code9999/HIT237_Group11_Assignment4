# create supervisors 

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model # for future proofing since get_user_model is more flexible than User object
from django.contrib.auth.models import Group
from django.utils import timezone

class Command(BaseCommand):
    help = "Create supervisor users"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Ensure the supervisor group exists
        supervisor_group, created = Group.objects.get_or_create(name='supervisor')

        # Define your supervisor users data
        supervisors_data = [
            {
                'username': 'yakub_sebastian',
                'password': 'yakub',
                'first_name': 'Yakub',
                'last_name': 'Sebastian',
                'email': 'yakubgroup11@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'supervisor'
            },
            {
                'username': 'bharanidharan_shanmugam',
                'password': 'bharanidharan',
                'first_name': 'Bharanidharan',
                'last_name': 'Shanmugam',
                'email': 'bharanidharangroup11@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'supervisor'
            },
            {
                'username': 'sami_azam',
                'password': 'sami',
                'first_name': 'Sami',
                'last_name': 'Azam',
                'email': 'samigroup11@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'supervisor'
            },
            {
                'username': 'asif_karim',
                'password': 'asif',
                'first_name': 'Asif',
                'last_name': 'Karim',
                'email': 'asifgroup11@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'supervisor'
            }
        ]

        for supervisor in supervisors_data:
            user, created = User.objects.get_or_create(
                username=supervisor['username'],
                defaults={
                    'first_name': supervisor['first_name'],
                    'last_name': supervisor['last_name'],
                    'email': supervisor['email'],
                    'date_joined': supervisor['date_joined'],
                    'user_type': supervisor['user_type']
                }
            )
            if created:
                user.set_password(supervisor['password'])
                user.save()
                user.groups.add(supervisor_group)
                self.stdout.write(self.style.SUCCESS(f"Supervisor {supervisor['username']} created successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Supervisor {supervisor['username']} already exists"))

        self.stdout.write(self.style.SUCCESS('Finished creating supervisor users'))
