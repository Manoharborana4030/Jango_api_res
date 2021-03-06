from urllib import response
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import IteamSSerializer
from rest_framework import viewsets, generics
from django.db.models import Sum


class restaurant(APIView):
	def get(self,request):
		obj = Restaurant.objects.all()
		serializer = RestaurantSerializer(obj,many=True)
		return Response(serializer.data)
	
	def post(self,request):
		serializer = RestaurantSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Restaurant has been added'})
		return Response(serializer.errors)

class cat(APIView):
	def get(self,request):
		obj = Cat_Res.objects.all()
		serializer = CatSerializer(obj,many=True)
		return Response(serializer.data)
	
	def post(self,request):
		serializer = CatSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'category has been added'})

class IteamData(GenericAPIView):
    serializer_class=IteamSSerializer
    permission_classes = (IsAuthenticated,)    
    def get(self,request):
        iteam=Iteams.objects.all()
        serializer=IteamSSerializer(iteam,many=True)
        return Response(serializer.data)
       
    def post(self,request):
        serializer=IteamSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Inserted'})
        return(serializer.errors)

