from datetime import datetime
from rest_framework import generics, serializers, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime
from .filters import LogFilter
from checkin.models import Person, VehicleType, Vehicle, Log, Absence, Shift
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PersonSerializer, VehicleTypeSerializer,  VehicleSerializer, LogSerializer, AbsenceSerializer, ShiftSerializer
from filters.mixins import (
    FiltersMixin,
)
from django.utils.dateparse import parse_datetime
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_fields = ('direction', 'vehicle')
    filterset = LogFilter
    # filter_backends = (filters.OrderingFilter,)
    # ordering_fields = ('log_datetime')
    # filter_class = LogFilter

    # filter_mappings = {
    #     'start': 'log_datetime__gte',
    #     # 'update_ts__gte': 'log_datetime__lte',
    #     }

    # filter_backends = [DjangoFilterBackend, LogFilter,]

    ordering = ['direction','-log_datetime']
    # def list(self, request):
    #     queryset = Log.objects.all()
    #     direction = request.GET.get('direction')
    #     if direction:
    #         queryset = Log.objects.filter(direction=direction)
       
    #     plate = request.GET.get('plate')
    #     if plate:
    #         queryset = Log.objects.filter(vehicle=plate)
        
    #     from_datetime = request.GET.get('from_datetime', )
    #     if from_datetime:
    #         from_datetime = parse_datetime(from_datetime)
    #         queryset = Log.objects.filter(log_datetime__gte=from_datetime)

    #     to_datetime = request.GET.get('to_datetime', )
    #     if to_datetime:
    #         to_datetime = parse_datetime(to_datetime)
    #         queryset = Log.objects.filter(log_datetime__lte=to_datetime)

    #     serializer = LogSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Log.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = LogSerializer(user)
    #     return Response(serializer.data)


class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         print(data)
    #         serializer = ShiftSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse({'Error': 'Invalid Data'}, status=400)        # try:
        #     instance = Btilog.objects.get(pk=kwargs['pk'])
        #     serializer = serializers.BtilogSerializer(instance=instance,data=request.data)
        #     if serializer.is_valid():
        #         btilog=serializer.save()
        #         return Response(serializer.data,status=status.HTTP_200_OK)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # except Btilog.DoesNotExist:
        #     serializer = serializers.BtilogSerializer(data=request.data)
        # if serializer.is_valid():
        #     btilog=serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# class LogList(APIView):
#     def get(self):
#         logs = Log.objects.all()
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer

    # def post(self, request, pk):
    #     pass


# class LogDetail(generics.RetrieveDestroyAPIView):
#     queryset = Log.objects.all()
#     serializer_class = LogSerializer


# class MissionList(generics.ListCreateAPIView):
#     queryset = Mission.objects.all()
#     serializer_class = MissionSerializer


# class MissionDetail(generics.RetrieveDestroyAPIView):
#     queryset = Mission.objects.all()
#     serializer_class = MissionSerializer


