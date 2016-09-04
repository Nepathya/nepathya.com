from __future__ import unicode_literals

from django.db import models


class Feedback(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.email)

