from django.db import models
import os
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
JOP_TYB = [
    ('part time', 'part time'),
    ('full time', 'full time'), ]


def uplod_imege(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.titel, extension)


class job(models.Model):
    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE)
    titel = models.CharField(max_length=50)
    discribe = models.TextField(max_length=1000)
    exprince = models.IntegerField(default=1)

    job_tyb = models.CharField(max_length=15, choices=JOP_TYB)
    
    puplish_time = models.DateTimeField(auto_now=True)
    salary = models.IntegerField(default=5)
    vacancy = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    imege = models.ImageField(upload_to=uplod_imege)

    slug = models.SlugField(null=True, blank=True)

    def save(self, *arges, **kwarges):
        self.slug = slugify(self.titel)

        super(job, self).save(*arges, **kwarges)

    def __str__(self):
        return self.titel


class category (models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class aplly_job(models.Model):
    job = models.ForeignKey(
        job, related_name='aplly_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(null=True)
    cv = models.FileField(upload_to='apply/')
    about = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
