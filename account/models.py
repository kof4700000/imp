from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class IMPUser(User):
    tel = models.CharField(max_length=11, blank=True)
    mobile = models.CharField(max_length=11, blank=True)
    display_name = models.CharField(max_length=20, blank=True)
    office = models.CharField(max_length=20,blank=True)
    num = models.CharField(max_length=4,blank=True)
