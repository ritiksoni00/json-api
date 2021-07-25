from django.core.exceptions import PermissionDenied
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Userserializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .models import UserData
import json



class RegisterView(APIView):
    def post(self, request):
        serializer = Userserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "succesfully registerd!"})

class LoginView(APIView):
    def post(self, request):
        username =request.data['username']
        qs=UserData.objects.filter(username=username)
        try:
            user = UserData.objects.filter(username=username)[0]
        except IndexError:
            return Response({"Error: Record does not exist"
                          })
            
        data={'first_name':qs[0].first_name,'last_name': qs[0].last_name,'email': qs[0].email,'is_active': qs[0].is_active,'is_superuser': qs[0].is_superuser}
        
        serialized_user =  json.dumps(data)
        parsed_user_data = json.loads(serialized_user)
        
        return Response({'user' : parsed_user_data,
                          'message' :   'succesfully loged in'})

        
        

