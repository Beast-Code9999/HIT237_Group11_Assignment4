# Generated by Django 5.0.4 on 2024-05-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_remove_projectchangerequest_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectchangerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
