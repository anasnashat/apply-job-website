from django.db import models

# Create your models here.

class Info(models.Model):
     address = models.CharField(max_length=50)
     phone=  models.CharField(max_length=15)
     email = models.EmailField(max_length=25)
     
     


     class Meta:

          verbose_name = 'Info'
          verbose_name_plural = 'Infos'



     def __str__(self):
          return self.email