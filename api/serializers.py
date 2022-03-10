from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Cat_Res,Restaurant,Iteams
from django.contrib.auth.models import User

from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = '__all__' 

class CatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cat_Res
		fields = '__all__' 