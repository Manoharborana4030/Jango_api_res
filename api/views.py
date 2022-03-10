from urllib import response
from rest_framework.generics import GenericAPIView
from .models import Restaurant,Cat_Res,Iteams
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import IteamSSerializer
from rest_framework import viewsets, generics
from django.db.models import Sum



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