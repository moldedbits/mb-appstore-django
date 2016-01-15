from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AppResource(models.Model):
    resource_key = models.CharField(max_length=200)

    def __str__(self):
        return self.resource_key
