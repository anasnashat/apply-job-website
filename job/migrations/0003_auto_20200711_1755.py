# Generated by Django 3.0.4 on 2020-07-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_tyb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='discribe',
            field=models.TextField(max_length=1000),
        ),
    ]