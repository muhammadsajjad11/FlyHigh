from inspect import trace
import re
from typing import List

from . import flights_pb2_grpc
from . import flights_pb2
import grpc
import traceback
from google.protobuf.json_format import MessageToDict
from .models import Flight, FlightDetails, Seating
from .serializers import FlightSerializer, FlightDetailsSerializer, SeatingSerailizer

class FlightListener(flights_pb2_grpc.FlightsServicer):
    def getFlights(self, request, context):
        try:
            print("in server! \n")
            print("SELF", self)
            print("before dict in server \n", request)
            request = MessageToDict(request)
            print("AFTER dict in server \n", request)
            print("CONTEXT", context)
            queryset = Flight.objects.filter(id__gte=1)
            print("Flight query rn is :", queryset)
            response = FlightSerializer(data=queryset, many=True)
            print('response type isSSS ', type(response))
            if response.is_valid(raise_exception=False):
                print('serializer response is', response.data)
            else:
                print('Response is not valid (FLight) and here is what it has to say:', response.errors)
            print("Response DATa", response.data)
            for i in response.data:
                print('response to client for loop', i) 
                yield flights_pb2.FlightResponse(**i)
        except Exception as e:
            traceback.print_exc()

    def getDetails(self, request, context):
        try:
            request = MessageToDict(request)
            print('Flight detail request in server', request)
            # Flight.objects.get(pk=request)
            # queryset = f.choice_set.all(), context={'request': request}
            queryset = FlightDetails.objects.filter(id__gte=1)
            response = FlightDetailsSerializer(data=queryset, many=True)
            if response.is_valid():
                print('Response is valid and proceeding further')
            else:
                print('Response is not valid (FLightDetail) and here is what it has to say:', response.errors)
            for i in response.data:
                yield flights_pb2.DetailResponse(**i)
        except Exception as e:
            traceback.print_exc()
            # return(ExceptionString=e.args[0])

    def getSeats(self, request, context):
        try:
            request = MessageToDict(request)
            queryset = Seating.objects.filter(id__gte=1)
            response = SeatingSerailizer(data=queryset, many=True)
            if response.is_valid():
                print('Response is valid and proceeding further')
            else:
                print('Response is not valid (Seating) and here is what it has to say:', response.errors)
            for i in response.data:
                yield flights_pb2.SeatResponse(**i)
        except Exception as e:
            traceback.print_exc()
            # return(ExceptionString=e.args[0])
    
    def setFlights(self, request, context):
        try:
            request = MessageToDict(request)
            response = FlightSerializer(data=request)
            if response.is_valid():
                print('response valid in set flight in server, proceeding further')
            else:
                print('response not valid in set flight in server, printing errors', response.errors)
            response = Flight.objects.create(**request)
            returnResponse = {
                "success" : True
            }
            return flights_pb2.flightcreateresponse(**returnResponse)
        except Exception as e:
              traceback.print_exc()
            
    def setDetails(self, request, context):
        try:
            request = MessageToDict(request)
            s = request["flightfk"]
            # print('SSS', s)
            # print('type SSS', type(s))
            a = Flight.objects.get(id = s)
            request['flightfk'] = a
            response = FlightDetailsSerializer(data=request)
            if response.is_valid():
                print('response valid in set flight in server, proceeding further')
            else:
                print('response not valid in set flight in server, printing errors', response.errors)
            response = FlightDetails.objects.create(**request)
            returnResponse = {
                "success" : True
            }
            return flights_pb2.flightcreateresponse(**returnResponse)
        except Exception as e:
              traceback.print_exc()
              




def grpc_hook(server):
    flights_pb2_grpc.add_FlightsServicer_to_server(FlightListener(), server)