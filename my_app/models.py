
# Create your models here.
from django.db import models

class Restaurant(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)

  def __str__(self):
    return self.name