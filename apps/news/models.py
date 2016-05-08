from __future__ import unicode_literals

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    source = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title + ":" + str(self.date)


    class Meta:
        verbose_name_plural = "News"

# Create your models here.
