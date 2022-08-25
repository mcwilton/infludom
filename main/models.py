from django.db import models


# Create your models here.

class Influencer(models.Model):
    name = models.CharField(max_length=255)
