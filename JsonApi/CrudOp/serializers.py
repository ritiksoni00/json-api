# from django.serializers import Serialize
from django.db.models import fields
from rest_framework import serializers
from .models import Tasklist


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = ['id','user','title','body','created_on','updated_on']