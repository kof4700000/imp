from __future__ import unicode_literals

from django.db import models
from account.models import IMPUser

# Create your models here.
class System(models.Model):
    short_name = models.CharField(max_length=20, blank = True)
    full_name = models.CharField(max_length=50, blank = True, unique = True)

    def __str__(self):
        return self.short_name

class User_System(models.Model):
    roles = (('A','A'),('B','B'))
    user = models.ForeignKey(IMPUser)
    sys = models.ForeignKey(System)
    role = models.CharField(max_length=1, choices = roles, default='A')

    def __str__(self):
        return self.user.display_name + "-" + self.sys.short_name

class Host(models.Model):
    IP = models.GenericIPAddressField(blank = True, null = True, unique = True)
    host_name = models.CharField(max_length=50, blank = True)
    host_type = models.CharField(max_length=50, blank = True)
    system = models.ForeignKey(System)

    def __str__(self):
        return self.IP + "-" + self.system.short_name
