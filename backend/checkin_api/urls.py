from django.urls import path
from .views import (PersonViewSet, VehicleTypeViewSet, VehicleViewSet,
                    LogViewSet, MissionViewSet)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('persons', PersonViewSet, basename='persons')
router.register('vehicletypes', VehicleTypeViewSet, basename='vehicletypes')
router.register('vechicles', VehicleViewSet, basename='vehicles')
router.register('logs', LogViewSet, basename='logs')
router.register('missions', MissionViewSet, basename='missions')

# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Checkin API')
app_name = 'checkin_api'

urlpatterns = [
    
]

urlpatterns += router.urls


# urlpatterns = [
#     path('persons/<int:pk>/', PersonDetail.as_view(), name='detailcreate' ),
#     path('persons/', PersonList.as_view(), name='listcreate' ),
#     path('vehicles/<int:pk>/', VehicleDetail.as_view(), name='detailcreate'),
#     path('vehicles/', VehicleList.as_view(), name='listcreate'),
#     path('logs/<int:pk>/', LogDetail.as_view(), name='detailcreate'),
#     path('logs/', LogList.as_view(), name='listcreate'),
#     path('missions/<int:pk>/', MissionDetail.as_view(), name='detailcreate'),
#     path('missions/', MissionList.as_view(), name='listcreate'),

# ]
