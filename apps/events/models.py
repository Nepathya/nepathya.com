from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TicketLocation(models.Model):
    name = models.CharField(max_length=255)
    ticket_location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    venue = models.OneToOneField(Location)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_location = models.ManyToManyField(TicketLocation, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.name + ':' + self.venue.name
