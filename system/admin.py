from django.contrib import admin
from .models import User_System, System, Host

# Register your models here.
admin.site.register(User_System)
admin.site.register(System)
admin.site.register(Host)
