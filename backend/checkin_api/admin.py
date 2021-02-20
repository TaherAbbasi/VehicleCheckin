from django.contrib import admin
from . import models 

admin.site.register(models.Vehicle)
admin.site.register(models.Log)
admin.site.register(models.Person)
admin.site.register(models.Mission)