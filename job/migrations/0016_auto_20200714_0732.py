# Generated by Django 3.0.4 on 2020-07-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_auto_20200714_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplly_job',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
