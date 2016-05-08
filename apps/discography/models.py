from __future__ import unicode_literals

from django.db import models

class Track(models.Model):
    header = models.CharField(max_length=3)
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    # album = models.ForeignKey(Album, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=30)
    zero_byte = models.BooleanField(default=False)
    track = models.IntegerField()
    genre = models.CharField(max_length=255)
# Create your models here.
