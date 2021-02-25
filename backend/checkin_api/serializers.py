from django.db.models import fields
from rest_framework import serializers
from checkin.models import Person, VehicleType, Vehicle, Log, Absence, Shift
from django.shortcuts import get_object_or_404, get_list_or_404
import django

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields='__all__'


class LogSerializer(serializers.ModelSerializer):
    
    # shift_info = serializers.SerializerMethodField()
    # absence_info = serializers.SerializerMethodField()

    # def get_shift_info(self, obj):
    #     vehicle = get_object_or_404(Vehicle, pk=obj.vehicle)
    #     shifts = VehicleSerializer(vehicle).data['shifts']
    #     shifts =  get_list_or_404(Shift, pk__in=shifts)
    #     shift_objects = ShiftSerializer(shifts, many=True).data
    #     return shift_objects
      
    # def get_absence_info(self, obj):
    #     vehicle = get_object_or_404(Vehicle, pk=obj.vehicle)
    #     absences = vehicle.absence_set.all()
    #     absence_objects = AbsenceSerializer(absences, many=True).data
    #     return absence_objects

    class Meta:
        model = Log
        # fields = ['log_datetime', 'direction', 'vehicle', 'shift_info', 'absence_info']
        fields = ['log_datetime', 'direction', 'vehicle']


class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shift
        fields = '__all__'
    
    def create(self, validated_data):
        shift = Shift(**validated_data)
        try:
            shift.save()
        except:
            raise serializers.ValidationError("Times are not correct")
        return shift