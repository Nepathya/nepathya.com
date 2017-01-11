from __future__ import unicode_literals

from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=250)
    cover_image = models.ImageField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    released_date = models.DateField(blank=True, null=True)
    label = models.ForeignKey(Label)
    genre = models.ForeignKey(Genre, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class MusicStore(models.Model):
    name = models.CharField(max_length=250)
    icon = models.ImageField()
    url = models.URLField()
    album = models.ForeignKey(Album, related_name="music_store")

    def __str__(self):
        return self.name + '| ' + str(self.url)


class Track(models.Model):
    header = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    comment = models.CharField(max_length=30, blank=True, null=True)
    track = models.PositiveSmallIntegerField(blank=True, null=True)
    genre = models.ForeignKey(Genre, blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True)
    copyright = models.CharField(max_length=200, blank=True, null=True)
    album = models.ForeignKey(Album, blank=True, null=True, related_name='tracks')
    length = models.PositiveIntegerField(blank=True, null=True)
    released_date = models.DateField(blank=True, null=True)
    label = models.ForeignKey(Label, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mp3 = models.FileField(upload_to='tracks', blank=True, null=True)

    def __str__(self):
        return self.title
