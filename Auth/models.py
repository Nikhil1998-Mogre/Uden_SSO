from django.db import models

# Create your models here.
class info(models.Model):
    name = models.CharField()
    email = models.EmailField()
    phone = models.IntegerField()