# Generated by Django 3.0.4 on 2020-07-11 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20200712_0053'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='jobs',
            new_name='job',
        ),
    ]