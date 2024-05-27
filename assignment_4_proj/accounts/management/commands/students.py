from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model # for future proofing since get_user_model is more flexible than User object
from django.contrib.auth.models import Group
from django.utils import timezone


class Command(BaseCommand):
    help = "Create student users"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # To make sure that the student group exists
        student_group, created = Group.objects.get_or_create(name='student')

        # Where we define our students  that are going to be predefined
        students_data = [
            {
                'username': 'jason_lay',
                'password': 'jasonpassword',
                'first_name': 'Jason',
                'last_name': 'Lay',
                'email': 'jasonlayStudent@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'student'
            },
            {
                'username': 'micia_gusmao',
                'password': 'miciapassword',
                'first_name': 'Micia',
                'last_name': 'Gusmao',
                'email': 'miciagusmaoStudent@gmail.com',
                'date_joined': timezone.now(),
                'user_type': 'student'
            },
            # we can add more students in the student list of objects
        ]

        for student in students_data:
            user, created = User.objects.get_or_create(
                username=student['username'],
                defaults={
                    'first_name': student['first_name'],
                    'last_name': student['last_name'],
                    'email': student['email'],
                    'date_joined': student['date_joined'],
                    'user_type': student['user_type']
                }
            )
            if created:
                user.set_password(student['password'])
                user.save()
                user.groups.add(student_group)
                self.stdout.write(self.style.SUCCESS(f"Student {student['username']} created successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Student {student['username']} already exists"))

        self.stdout.write(self.style.SUCCESS('Finished creating student users'))