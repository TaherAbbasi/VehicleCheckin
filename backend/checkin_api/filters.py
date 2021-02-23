import django_filters
from checkin.models import Log

class LogFilter(django_filters.FilterSet):

    start = django_filters.DateTimeFilter(input_formats=['%Y-%m-%dT%H:%M:%S'], lookup_expr='gte', field_name="log_datetime")
    end = django_filters.DateTimeFilter(input_formats=['%Y-%m-%dT%H:%M:%S'], lookup_expr='lte', field_name="log_datetime")

    class Meta:
        model = Log
        fields = ['log_datetime']
