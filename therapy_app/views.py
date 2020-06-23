from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from . import models
from .authentication_classes import CsrfExemptSessionAuthentication
from .permissions import *


# Create your views here.
class LoginView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [NotAuthenticated]

    def post(self, request, format=None):
        data = request.data

        username = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active and (not user.is_deleted):
                login(request, user)
                return Response({"message": "You are logged in successfully."}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': "Please provide proper email and password."}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "successfully logged out."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You are not logged in."}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [NotAuthenticated]

    def post(self, request, format=None):
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)
        user_type = data.get('type', None)

        try:
            if email and password and (user_type in ['Client', 'Therapist']):
                user = models.User.objects.create_user(email=email, password=password, type=user_type)
                return Response({"message": "Your account has been created successfully. Please Login."},
                                status=status.HTTP_200_OK)
            else:
                raise Exception
        except Exception as e:
            # this will be executed when any one value is null or when an Integrity Error is thrown
            return Response({'error': "Please provide proper email, password, and type."},
                            status=status.HTTP_400_BAD_REQUEST)
