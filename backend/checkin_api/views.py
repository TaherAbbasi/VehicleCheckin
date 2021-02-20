from rest_framework import generics, serializers
from .models import Person, Vehicle, Log, Mission
from .serializers import PersonSerializer, VehicleSerializer, LogSerializer, MissionSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    # def post(self, request, pk):
    #     pass


class LogDetail(generics.RetrieveDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class MissionList(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionDetail(generics.RetrieveDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


