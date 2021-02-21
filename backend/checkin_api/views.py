from rest_framework import generics, serializers, viewsets
from checkin.models import Person, VehicleType, Vehicle, Log, Mission

from .serializers import PersonSerializer, VehicleTypeSerializer,  VehicleSerializer, LogSerializer, MissionSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = PersonSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


# class PersonList(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


# class PersonDetail(generics.RetrieveDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


# class VehicleList(generics.ListCreateAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer


# class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer


# class LogList(generics.ListCreateAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer

#     # def post(self, request, pk):
#     #     pass


# class LogDetail(generics.RetrieveDestroyAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer


# class MissionList(generics.ListCreateAPIView):
#     queryset = Mission.objects.all()
#     serializer_class = MissionSerializer


# class MissionDetail(generics.RetrieveDestroyAPIView):
#     queryset = Mission.objects.all()
#     serializer_class = MissionSerializer


