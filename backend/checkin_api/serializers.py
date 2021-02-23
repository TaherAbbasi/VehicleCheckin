from django.db.models import fields
from rest_framework import serializers
from checkin.models import Person, VehicleType, Vehicle, Log, Absence, Shift

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
    vehicle = VehicleSerializer(read_only=True)
    class Meta:
        model = Log
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