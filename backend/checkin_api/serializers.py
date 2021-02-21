from django.db.models import fields
from rest_framework import serializers
from checkin.models import Person, VehicleType, Vehicle, Log, Mission

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields='__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'