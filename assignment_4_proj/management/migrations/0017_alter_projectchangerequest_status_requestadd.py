# Generated by Django 5.0.4 on 2024-05-28 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_alter_projectchangerequest_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectchangerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('Rejected', 'rejected')], default='pending', max_length=20),
        ),
        migrations.CreateModel(
            name='RequestAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('topic_num', models.PositiveIntegerField(null=True, unique=True, verbose_name='Topic number')),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('Rejected', 'rejected')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ManyToManyField(blank=True, to='management.category')),
                ('location', models.ManyToManyField(blank=True, to='management.location')),
                ('research_areas', models.ManyToManyField(blank=True, to='management.researcharea')),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
