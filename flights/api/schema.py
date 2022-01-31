from asyncio import ThreadedChildWatcher
from django.forms import fields
import graphene
from graphene_django import DjangoObjectType

from . models import Flight, FlightDetails, Seating

class FlightType(DjangoObjectType):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightDetailType(DjangoObjectType):
    class Meta:
        model = FlightDetails
        fields = '__all__'

class Query(graphene.ObjectType):
    flights = graphene.List(FlightType)
    # all_flights = graphene.List(FlightType)
    # category_by_name = graphene.Field(FlightType, name = graphene.String(required=True))

    def resolve_flights(self, root, info, **kwargs):
        return Flight.objects.all()

    # def resolve_by_name(root, info, airlineName):
    #     try:
    #         return Flight.objects.get(airlineName = airlineName)
    #     except Flight.DoesNotExist:
    #         return None
    
schema = graphene.Schema(query=Query)