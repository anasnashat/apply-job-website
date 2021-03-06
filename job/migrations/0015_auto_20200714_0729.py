# Generated by Django 3.0.4 on 2020-07-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='aplly_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('about', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='exprince',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=5),
        ),
    ]
