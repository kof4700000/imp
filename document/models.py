from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    doc_name = models.CharField(max_length = 128)
    tag = models.CharField(max_length = 128)
    src = models.CharField(max_length = 128, blank=True)

    def __str__(self):
        return self.doc_name
