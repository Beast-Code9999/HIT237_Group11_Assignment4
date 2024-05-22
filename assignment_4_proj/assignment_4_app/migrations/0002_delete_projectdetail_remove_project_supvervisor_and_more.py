# Generated by Django 5.0.4 on 2024-05-22 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_4_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectDetail',
        ),
        migrations.RemoveField(
            model_name='project',
            name='supvervisor',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='location name'),
        ),
        migrations.AddField(
            model_name='project',
            name='research_area',
            field=models.CharField(max_length=100, null=True, verbose_name='Fields of study'),
        ),
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='assignment_4_app.supervisor'),
        ),
        migrations.AddField(
            model_name='project',
            name='topic_num',
            field=models.IntegerField(null=True, verbose_name='Topic number'),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='First name(s)'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Last name'),
        ),
        migrations.AddField(
            model_name='student',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='assignment_4_app.project'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=20, null=True, verbose_name='Student ID'),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='members',
            field=models.ManyToManyField(null=True, related_name='student_groups', to='assignment_4_app.student'),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assignment_4_app.project'),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='First name(s)'),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Last name'),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='staff_id',
            field=models.CharField(max_length=20, null=True, verbose_name='Staff ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]