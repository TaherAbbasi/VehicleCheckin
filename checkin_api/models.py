from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
from django.utils import timezone
from datetime import datetime    

class Person(models.Model):
    
    name = models.CharField(max_length=40)
    personnel_id = models.PositiveIntegerField(blank=False, null=False, unique=True)
    
    def __str__(self) -> str:
        return self.name

class Vehicle(models.Model):
    
    plate_no = models.CharField(max_length=8, blank=False, null=False)
    rfid_no = models.PositiveBigIntegerField(unique=True)
    driver =  models.ForeignKey(
        Person, on_delete=models.PROTECT, null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{str(self.plate_no)}'

class Log(models.Model):
    
    options = (('enter', 'Enter'),
                ('exit', 'Exit')
                )
    log_datetime = models.DateTimeField()
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.PROTECT, null=False, blank=False,
        default=datetime.now())
    direction = models.CharField(
            max_length=10, choices=options, default='Enter'
    )
    def __str__(self) -> str:
        enter_or_exit = 'Entered at' if self.direction=='enter' else 'Exited at'
        return f'{self.vehicle} {enter_or_exit} {str(self.log_datetime.date())}\
        {str(self.log_datetime.time())}'

class Mission(models.Model):

    from_datetime = models.DateTimeField(blank=False, null=False)
    to_datetime = models.DateTimeField(blank=False, null=False)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.PROTECT, null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.vehicle}_{str(self.from_datetime.date())}\
            {str(self.from_datetime.time())}_{str(self.to_datetime.date())}\
            {str(self.to_datetime.time())}'