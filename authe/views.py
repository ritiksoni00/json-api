from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import RegisterSerializers
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializers

    def post(self, request, *arg, **kwa):
        seri = self.serializer_class(data=request.data)
        if seri.is_valid():
            user = seri.save()
            ref_tok = RefreshToken.for_user(user)
            data = {
                "refres": str(ref_tok),
                "access": str(ref_tok.access_token),
                "user": seri.data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(seri.errors, status=status.HTTP_401_UNAUTHORIZED)
