import json
from datetime import datetime
from django.db.models.base import Model

from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils.dateparse import parse_datetime
from .filters import LogFilter
from checkin.models import Person, VehicleType, Vehicle, Log, Absence, Shift
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (PersonSerializer, VehicleTypeSerializer,  VehicleSerializer, 
                        LogSerializer, AbsenceSerializer, ShiftSerializer)
from filters.mixins import (
    FiltersMixin,
)
from django.utils.dateparse import parse_datetime
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import django

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
    ordering = ['direction','-log_datetime']

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        plate = request.POST.get('vehicle')
        direction = request.POST.get('direction')
        if plate and (direction in ('enter', 'exit')):
            vehicle = get_object_or_404(Vehicle, pk=plate)
            shifts = VehicleSerializer(vehicle).data.get('shifts')
            shifts = get_list_or_404(Shift, pk__in=shifts)
            shifts = [ShiftSerializer(s).data for s in shifts]
            log_time = request.POST.get('log_time')
            if direction=='enter':
                direction = 'entrance'
            in_shift_range = False
            is_log_unique = False
            for s in shifts:
                if (log_time > s[direction + '_low_range']) and \
                   (log_time < s[direction + '_high_range']):
                    in_shift_range = True
                    log_date = request.POST.get('log_date')
                    log = Log.objects.filter(log_date=log_date,
                        log_time__gte=s[direction + '_low_range'],
                        log_time__lte=s[direction + '_high_range']).first()
                    if not log:
                        is_log_unique = True
                        break

            data = serializer.validated_data
            data['vehicle'] = plate
            if (not in_shift_range):
                data['Error'] = 'Not in shift range'    
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if (not is_log_unique):
                data['Error'] = 'Logged Before'
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    filter_fields = ('absence_type', 'vehicle')


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class FullLogList(generics.ListAPIView):


    def list(self, request, *args, **kwargs):
        queryset = Log.objects.all()
        direction = request.GET.get('direction')
        shifts = None
        if direction:
            queryset = queryset.filter(direction=direction)
       
        plate = request.GET.get('plate')
        if plate:
            queryset = queryset.filter(vehicle=plate)
            vehicle = get_object_or_404(Vehicle, pk=plate)
            
            shifts = VehicleSerializer(vehicle).data.get('shifts')
            shifts = get_list_or_404(Shift, pk__in=shifts)
            shifts = [ShiftSerializer(s).data for s in shifts]
            
            absences = django.core.serializers.serialize('json', 
                list(Absence.objects.filter(vehicle=plate)), 
                fields=('absence_type', 'from_datetime', 'to_datetime'),
                ensure_ascii=False)
            
            absences = json.loads(absences)
            absences = [a['fields'] for a in absences]
        
        from_datetime = request.GET.get('from_datetime')
        if from_datetime:
            from_datetime = parse_datetime(from_datetime)
            queryset = queryset.filter(log_date__gte=from_datetime.date())
            queryset = queryset.filter(log_time__gte=from_datetime.time())

        to_datetime = request.GET.get('to_datetime')
        if to_datetime:
            to_datetime = parse_datetime(to_datetime)
            queryset = queryset.filter(log_date__lte=to_datetime.date())
            queryset = queryset.filter(log_time__lte=to_datetime.time())

        logs = LogSerializer(queryset, many=True).data
        
        return Response({
            "log": logs,
            "absences": absences,
            "shifts": shifts,
        })