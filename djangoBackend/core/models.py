from django.db import models

# Create your models here.
class Demo(models.Model):
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=100)