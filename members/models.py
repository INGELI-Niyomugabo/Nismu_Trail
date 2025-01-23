from django.db import models


# Create your models here.
class member(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    images_url = models.CharField(max_length=2083)


class result(models.Model):
    score = models.FloatField()
    comment = models.CharField(max_length=4000)
    reward = models.FloatField(max_length=255)
