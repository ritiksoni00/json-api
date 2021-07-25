from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import UserData

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['username','first_name','last_name','email','is_active','is_superuser','password']

    
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserData
#         fields = ['email', 'password']