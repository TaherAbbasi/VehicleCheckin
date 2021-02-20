# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class Person(models.Model):
    
#     name = models.CharField(max_length=40)
#     personnel_id = models.PositiveIntegerField(blank=False, null=False, unique=True)
    
#     def __str__(self) -> str:
#         return self.name

# class Vehicle(models.Model):
    
#     plate_no = models.CharField(max_length=8, blank=False, null=False)
#     rfid_no = models.PositiveBigIntegerField(unique=True)
#     driver =  models.ForeignKey(
#         Person, on_delete=models.PROTECT, null=False, blank=False)
    
#     def __str__(self) -> str:
#         return f'{str(self.plate_no)}'

# class Log(models.Model):

#     in_datetime = models.DateTimeField()
#     out_datetime = models.DateTimeField()
#     vehicle = models.ForeignKey(
#         Vehicle, on_delete=models.PROTECT, null=False, blank=False)
    
#     def __str__(self) -> str:
#         return f'{self.vehicle}_{str(self.in_datetime.date())}\
#         {str(self.in_datetime.time())}_{str(self.out_datetime.date())}\
#         {str(self.out_datetime.time())}'

# class Mission(models.Model):

#     from_datetime = models.DateTimeField(blank=False, null=False)
#     to_datetime = models.DateTimeField(blank=False, null=False)
#     vehicle = models.ForeignKey(
#         Vehicle, on_delete=models.PROTECT, null=False, blank=False)
    
#     def __str__(self) -> str:
#         return f'{self.vehicle}_{str(self.from_datetime.date())}\
#             {str(self.from_datetime.time())}_{str(self.to_datetime.date())}\
#             {str(self.to_datetime.time())}'