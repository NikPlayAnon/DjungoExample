from django.db import models

# Create your models here.
class Members(models.Model):
  PhoneNum = models.CharField(max_length=255)
  Timeline = models.CharField(max_length=255)