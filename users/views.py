from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.


@api_view(["POST"])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        auth_token, _ = Token.objects.get_or_create(user=user)
        return Response({"token":auth_token.key}, status=HTTP_200_OK)
    else:
        return Response({"error: Wrong Credentials"}, status=HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        request.user.auth_token.delete()
        return Response({"message": "Logout"}, status=HTTP_200_OK)
    except Exception as e:
        return Response({"error":str(e)}, status=HTTP_400_BAD_REQUEST)
        