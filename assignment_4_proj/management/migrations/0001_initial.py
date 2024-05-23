# Generated by Django 5.0.4 on 2024-05-23 07:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('topic_num', models.PositiveIntegerField(null=True, verbose_name='Topic number')),
                ('location', models.CharField(max_length=100, null=True, verbose_name='location')),
                ('research_areas', models.CharField(max_length=100, null=True, verbose_name='Fields of study')),
                ('description', models.TextField(blank=True)),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]