from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True, null=True)


class Track(models.Model):
    header = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=30, blank=True, null=True)
    zero_byte = models.BooleanField(default=False)
    track = models.IntegerField()
    genre = models.CharField(max_length=255)
    album_art = models.ImageField(blank=True, null=True)
    copyright = models.CharField(max_length=200, blank=True, null=True)


class Discography(models.Model):
    album = models.ForeignKey(Album, blank=True, null=True)
    album_version = models.CharField(max_length=50, blank=True, null=True)
    track = models.ForeignKey(Track, blank=True, null=True)
