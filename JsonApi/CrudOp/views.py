from .models import Tasklist
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import permissions


class CreateTask(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer
    def post(self, request):
        data = TaskSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data ,status=201)
        return Response(data={'not created'}, status=status.HTTP_400_BAD_REQUEST)

class DeleteTask(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = TaskSerializer

    def get_object(self, id):
        try:
            return Tasklist.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
    def get(self, request, id):
        data = self.serializer_class(self.get_object(id))
        return Response(data.data, status=status.HTTP_200_OK)

class ViewAllTask(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = TaskSerializer
    """For Api Viwes
    code
    """
    
    # def get(self, request):
    #     tasks = Tasklist.objects.all()
    #     data = self.serializer_class(tasks, many=True)
    #     return Response(data.data, status=status.HTTP_200_OK)

    """"for generics api views"""
    queryset = Tasklist.objects.all()
    


