from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Airport
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.serializers import AirportSerializer

# Create your views here.
'''
def airports(req):
	ports = Airport.objects.all()
	data = [(port.name,port.lat,port.log) for port in ports]
	return HttpResponse(json.dumps(data))
'''
class AirportView(APIView):
	authentication_classes=[]
	permission_classes=[]
	def get(self,request,pk=None,format=None):
		ports = Airport.objects.all()
		#data = [(port.name,port.lat,port.log) for port in ports]
		ser=AirportSerializer(data=ports, many=True)
		ser.is_valid()
		data=ser.data
		return Response(data)
	def put(self,request,pk,format=None):
		port = Airport.objects.get(id=pk)
		data = self.request.data
		if "lat" in data:
			port.lat=data.get("lat")
		if "log" in data:
			port.log=data.get("log")
		if "name" in data:
			port.name=data.get("name")
		port.save()
		resp = Response("port updated successfully!!")
		print(resp)
		return resp
	def delete(self,request,pk,format=None):
		port = Airport.objects.get(id=pk)
		port.delete()
		return Response("port deleted successfully!!")
	def post(self,request,format=None):
		data=self.request.data
		#airport = Airport(**data)
		# airport=Airport(name=data.get("air_name"),
		# 	lat=data.get("air_lat"),
		# 	log=data.get("air_log"))
		airport = Airport(**data)
		airport.save()
		return Response("Airport created successfully!!")
