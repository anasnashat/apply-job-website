# Generated by Django 3.0.4 on 2020-07-11 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='job',
            new_name='jobs',
        ),
    ]