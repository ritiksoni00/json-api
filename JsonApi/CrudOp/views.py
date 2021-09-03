from http.client import BAD_REQUEST
import re
from django.shortcuts import render 
from .models import Tasklist
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView 
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.permissions import IsAuthenticated


class CreateTask(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    def post(self, request):
        data = TaskSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data ,status=201)
        return Response(data={'not created'}, status=status.HTTP_400_BAD_REQUEST)

class DeleteTask(GenericAPIView):
    def get_object(self, id):
     try:
         return Tasklist.objects.get(id=id)
     except ObjectDoesNotExist:
         raise Http404
    def delete(self, request, id):
        task=self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UpdateTask(GenericAPIView):
    serializer_class = TaskSerializer
    def get_object(self, id):
     try:
         return Tasklist.objects.get(id=id)
     except ObjectDoesNotExist:
         raise Http404
    def put(self, request, id):
        task = self.get_object(id)
        data = self.serializer_class(task, data=request.data)
        if data.is_valid():
            data.save()
            seri_data =data.data 
            return Response(seri_data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    

class ViewTask(GenericAPIView):
    serializer_class = TaskSerializer

    def get_object(self, id):
        try:
            return Tasklist.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
    def get(self, request, id):
        data = self.serializer_class(self.get_object(id))
        return Response(data.data, status=status.HTTP_200_OK)

class ViewAllTask(APIView):
    # permission_classes = [IsAuthenticated]

    serializer_class = TaskSerializer

    def get(self, request):
        tasks = Tasklist.objects.all()
        data = self.serializer_class(tasks, many=True)
        return Response(data.data, status=status.HTTP_200_OK)


