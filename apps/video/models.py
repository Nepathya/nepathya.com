from __future__ import unicode_literals

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=250)
    youtube_id = models.CharField(max_length=250, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)

# Create your models here.
