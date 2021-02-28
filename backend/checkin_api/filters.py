import django_filters
from checkin.models import Log

class LogFilter(django_filters.FilterSet):

    start_date = django_filters.DateFilter(input_formats=['%Y-%m-%d'], lookup_expr='gte', field_name="log_date")
    start_time = django_filters.TimeFilter(input_formats=['%H:%M:%S'], lookup_expr='gte', field_name="log_time")
    end_date = django_filters.DateFilter(input_formats=['%Y-%m-%d'], lookup_expr='lte', field_name="log_date")
    end_time = django_filters.TimeFilter(input_formats=['%H:%M:%S'], lookup_expr='lte', field_name="log_time")

    class Meta:
        model = Log
        fields = ['log_date',
                 'log_time',
                 ]
