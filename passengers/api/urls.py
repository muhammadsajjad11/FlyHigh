from django.urls import path, include
from rest_framework import routers, urlpatterns

from . import views

router = routers.DefaultRouter()
router.register(r'check', views.Flights, basename='check')
router.register(r'flightdetailz', views.FlightDetails, basename='detailscheck')




urlpatterns = [
    path('', include(router.urls)),
    # path('flightdetails/<int:id>', views.FlightDetails.as_view(
    #         {
    #             'get':'list'
    #         }
    #     ),name='flight-details'),
    # path('', include(router.urls)),
    # path('check', views.Flights.as_view(
    #     {
    #         'get':'list',
    #         'post':'create'
    #    }
    # ))
]