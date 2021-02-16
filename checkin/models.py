from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Person(models.Model):
    
    name = models.CharField(max_length=40)
    personnel_id = models.PositiveIntegerField(blank=False, null=False, unique=True)

class Vehicle(models.Model):
    
    plate_no = models.CharField(max_length=8, blank=False, null=False)
    rfid_no = models.PositiveBigIntegerField(unique=True)
    driver =  models.ForeignKey(
        Person, on_delete=models.PROTECT, null=False, blank=False)

class Log(models.Model):

    in_datetime = models.DateTimeField()
    out_datetime = models.DateTimeField()
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.PROTECT, null=False, blank=False)

class Mission(models.Model):

    from_datetime = models.DateTimeField(blank=False, null=False)
    to_datetime = models.DateTimeField(blank=False, null=False)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.PROTECT, null=False, blank=False)