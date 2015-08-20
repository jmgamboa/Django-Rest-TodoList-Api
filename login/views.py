from django.shortcuts import render
from django.contrib.auth.models import User
from serializers import UserSerializer
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from authentication import QuietBasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view


class AuthView(APIView):
    """
    Password authentication via basic auth
    """
    authentication_classes = (QuietBasicAuthentication,)
    def post(self, request, *args, **kwargs):
        try:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            login(request, user)
            return Response(UserSerializer(user).data['username'])
        except AttributeError:
            return HttpResponse("wrong password or username")


class CreateUserView(APIView):
    serializers = UserSerializer
    def post(self, request, *args, **kwargs):
        """
        Create User and Validate Field
        """
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.data['username'],
                serialized.data['email'],
                serialized.data['password']
            )
            return Response(serialized.data['username'], status="201 Created")
        else:
            return Response(serialized._errors, status="400 Bad Request")


def logout_user(request):
    """
    Log out session
    """
    logout(request)
    return redirect('/index')
