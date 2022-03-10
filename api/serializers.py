from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Cat_Res,Restaurant,Iteams
from django.contrib.auth.models import User

class IteamSSerializer(serializers.ModelSerializer):
    class Meta:
        model=Iteams
        fields='__all__'

class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = '__all__' 

class CatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cat_Res
		fields = '__all__' 
