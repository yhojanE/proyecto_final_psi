from django.db import models

# Create your models here.
class Practica(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    imagen_url = models.URLField(blank=True, null=True)


    def _str_(self):
        return self.username
    