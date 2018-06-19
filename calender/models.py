from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length = 100, blank = True)
    backgroundColor = models.CharField(max_length = 6)
    borderColor = models.CharField(max_length = 6)
    #tag = models.CharField(max_length = 20)
    #start = models.DateTimeField()
    #end = models.DateTimeField()
    start_y = models.IntegerField(default = 2018)
    start_m = models.IntegerField(default = 1)
    start_d = models.IntegerField(default = 1)
    end_y = models.IntegerField(default = 2018)
    end_m = models.IntegerField(default = 1)
    end_d = models.IntegerField(default = 1)

    def __str__(self):
        return self.title
