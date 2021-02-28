from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.db.models.fields import BooleanField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import CheckConstraint, Q, F
import django

class Person(models.Model):
    
    options = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    personnel_id = models.PositiveIntegerField(blank=False, null=False, primary_key=True)
    phone = PhoneNumberField(help_text='Contact Phone Number', verbose_name='Phone', blank=False, null=False)
    contract_expire_date = models.DateField(verbose_name='Contract Expire Date')
    contract_status = models.CharField(max_length=10, choices=options, verbose_name='Contract Status')
    account_no = models.PositiveIntegerField(verbose_name='Account No')

    def __str__(self):
        return self.name


class VehicleType(models.Model):

    name = models.CharField(max_length=30, blank=False, unique=True, null=False)

    def __str__(self):
        return self.name


class Shift(models.Model):

    name = models.CharField(max_length=30, blank=False, null=False, primary_key=True)
    entrance_time = models.TimeField(null=False, blank=False, verbose_name='Enter')
    entrance_low_range = models.TimeField(null=False, blank=False, verbose_name='Enter Low Range')
    entrance_high_range = models.TimeField(null=False, blank=False, verbose_name='Enter High Range')
    exit_time = models.TimeField(null=False, blank=False, verbose_name='Exit')
    exit_low_range = models.TimeField(null=False, blank=False, verbose_name='Exit Low Range')
    exit_high_range = models.TimeField(null=False, blank=False, verbose_name='Exit High Range')

    class Meta:
        unique_together = ('entrance_time', 'exit_time',)
        constraints = [
            CheckConstraint(
                check = Q(entrance_time__lt=F('exit_time'),
                entrance_time__gt=F('entrance_low_range'), 
                entrance_high_range__gt=F('entrance_time'), 
                exit_time__gt=F('exit_low_range'), 
                exit_high_range__gt=F('exit_time'),
                ), 
                name = 'check_enter_and_exit_times',
            ),
        ]
    
    def __str__(self):
        return self.name


class Vehicle(models.Model):
    
    driver_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Driver Name')
    driver_phone = PhoneNumberField(blank=False, null=False, help_text='Driver Phone Number', verbose_name='Phone')
    plate_no = models.CharField(max_length=8, blank=False, null=False, primary_key=True, verbose_name='Plate No.')
    rfid_no = models.CharField(max_length=100, blank=False, null=False, unique=True, verbose_name='RFID No.')
    owner =  models.ForeignKey(
        Person, on_delete=models.PROTECT, null=False, blank=False)
    v_class = models.ForeignKey(VehicleType, models.PROTECT, verbose_name='Class')
    transition_path = models.CharField(max_length=200, verbose_name='Path')
    driver_license_exp = models.DateField(verbose_name='License Exp.')
    insurance_exp = models.DateField(verbose_name='Insurance Exp.')
    intelligent_card_exp = models.DateField(verbose_name='Intelligent Card Exp.')
    health_card_exp = models.DateField(verbose_name='Health Card Exp.')
    inspection_exp = models.DateField(verbose_name='Inspection Exp.')
    shifts = models.ManyToManyField(Shift)

    def __str__(self):
        return f'{str(self.plate_no)}'


class Log(models.Model):
    
    options = (('enter', 'Enter'),
                ('exit', 'Exit'),
                )
    log_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d") , null=False, blank=False, verbose_name='Log Date')
    log_time = models.TimeField(default=datetime.now().strftime("%H:%M:%S") , null=False, blank=False, verbose_name='Log Time')
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.PROTECT, null=False, blank=False,
        )
    direction = models.CharField(
            max_length=10, choices=options, null=False, blank=False
    )
    class Meta:
        ordering = ["-log_date", '-log_time']
        unique_together = ('log_date', 'log_time', 'vehicle',)

    
    def __str__(self):
        enter_or_exit = 'Entered at' if self.direction=='enter' else 'Exited at'
        return f'{self.vehicle} {enter_or_exit} {str(self.log_date)}\
        {str(self.log_time)}'


class Absence(models.Model):
    
    options = (
        ('mission', 'Mission'),
        ('absence', 'Absence'),
        ('leave', 'Leave'),
    )
    from_datetime = models.DateTimeField(blank=False, null=False, verbose_name='From')
    to_datetime = models.DateTimeField(blank=False, null=False, verbose_name='To')
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.PROTECT, null=False, blank=False)
    absence_type = models.CharField(
            max_length=10, choices=options, null=False, blank=False
    )

    class Meta:
        constraints = [
            CheckConstraint(
            check = Q(to_datetime__gt=F('from_datetime'),),
            name='to_datetime_gt_than_from_datetime')
        ]
    
    def __str__(self):
        return f'{self.vehicle}_{str(self.from_datetime.date())}\
            {str(self.from_datetime.time())}_{str(self.to_datetime.date())}\
            {str(self.to_datetime.time())}'
