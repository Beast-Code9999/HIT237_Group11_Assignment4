# Generated by Django 5.0.4 on 2024-05-23 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_4_app', '0007_alter_project_topic_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='studentgroup',
            name='project',
        ),
        migrations.RemoveField(
            model_name='student',
            name='project',
        ),
        migrations.DeleteModel(
            name='ProjectApplication',
        ),
        migrations.RemoveField(
            model_name='studentgroup',
            name='members',
        ),
        migrations.DeleteModel(
            name='Supervisor',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentGroup',
        ),
    ]
