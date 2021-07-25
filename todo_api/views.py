from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class GetAllTodo(APIView):
    permission_classes = [ IsAuthenticated]
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)


class GetTodo(APIView):
    permission_classes = [ IsAdminUser]
    def get(self, request, id):
        try:            
            instance = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({"Does not Exixts"}, status = 404)
        serializer = TodoSerializer(instance)
        return JsonResponse(serializer.data, status = 201)
       




class CreatTodo(APIView):
    permission_classes = [ IsAdminUser]
    @csrf_exempt
    def post(self, request):
        parsed = JSONParser()
        data = parsed.parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg" :"created "}, status = 201)
        return JsonResponse(serializer.errors, status = 400)


class UpdateTodo(APIView):
    permission_classes = [ IsAdminUser]
    def put(self, request, id ):
        try:
            instance = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({"Does not Exixts"}, status = 404)
        parsed = JSONParser()
        data = parsed.parse(request)
        serializer = TodoSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, staus = 400)


class DeleteTodo(APIView):
    permission_classes = [ IsAdminUser]
    def delete(self, request, id):
        try:
            instance = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({"Does not Exixts" : 'no'}, status = 404)
        
        instance.delete()
        return JsonResponse({"succefully" : 'deleted'}, status=204)

        
        
        

