from urllib import response
from rest_framework.generics import GenericAPIView
from .models import Restaurant,Cat_Res,Iteams
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import all_iteam_with_cat_using_res_Serializer,Res_Greater_500_Serializer,Restaurant_details_with_count_Serializer,IteamListSerializer,UserSerializer,Cat_resSerializer, RestaurantSerializer,IteamSSerializer,CustomeIteamSSerializer
from rest_framework import viewsets, generics
from django.db.models import Sum



