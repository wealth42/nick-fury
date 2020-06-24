from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from . import models
from .authentication_classes import CsrfExemptSessionAuthentication
from .permissions import *
from . import serializers


# Create your views here.
class LoginView(APIView):
    """
    This APIView takes POST request only to log users into the session
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [NotAuthenticated]

    def post(self, request, format=None):
        """
        This method logs user into the session.
        Required params:
            email - user's email
            password - user's password
        """
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
    """
    This APIView is to log users out of the session.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        This method logs out authenticated user.
        """
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "successfully logged out."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You are not logged in."}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    """
    This APIView is intended to create new users.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [NotAuthenticated]

    def post(self, request, format=None):
        """
        This is used to create new users
        Required form-data:
            email - must be an email
            password
            type - must be either 'Client' or 'Therapist'
        """
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


class ChatView(APIView):
    """
    This APIView is intended to POST message and GET list of message.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsClient | IsTherapist]

    def get(self, request, id1, format=None):
        """
        This method will chat history of requesting user and corresponding mapped user.
        """
        if models.User.objects.exclude(pk=request.user.pk).filter(is_deleted=False, pk=id1).exists():
            try:
                if request.user.type == "Client":
                    mapping = models.Mapping.objects.get(is_deleted=False, client=request.user, therapist__id=id1)
                elif request.user.type == "Therapist":
                    mapping = models.Mapping.objects.get(is_deleted=False, client__id=id1, therapist=request.user)
                if mapping:
                    chats = models.Chat.objects.filter(is_deleted=False).filter(
                        (Q(from_user=request.user) & Q(to_user__id=id1)) |
                        (Q(to_user=request.user) & Q(from_user__id=id1))).order_by('created_at')
                    serialized = serializers.ChatSerializer(chats, many=True)
                    return Response(serialized.data, status=status.HTTP_200_OK)
                else:
                    raise Exception
            except Exception as e:
                return Response({'data': 'There does not exist such an active mapping.'},
                                status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response({'message': 'No such User (therapist or client) exists'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, id1, format=None):
        """
        This will be executed on POST requests.
        Required Parameters:
            - message - Character string
        """
        if models.User.objects.exclude(pk=request.user.pk).filter(is_deleted=False, pk=id1).exists():
            try:
                if request.user.type == "Client":
                    mapping = models.Mapping.objects.get(is_deleted=False, client=request.user, therapist__id=id1)
                elif request.user.type == "Therapist":
                    mapping = models.Mapping.objects.get(is_deleted=False, client__id=id1, therapist=request.user)
                if mapping:
                    serialized = serializers.ChatSerializer(data={
                        "from_user": request.user.pk,
                        "to_user": id1,
                        "message": request.data.get('message')
                    })
                    if serialized.is_valid():
                        serialized.save()
                        return Response({"message": "Your message has been sent.",
                                         "from_user": request.user.pk,
                                         "to_user": id1,
                                         "your message": request.data.get('message')},
                                        status=status.HTTP_200_OK)
                    else:
                        return Response({"message": "Your message can not be sent"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    raise Exception
            except Exception as e:
                return Response({'data': 'There does not exist such an active mapping.'},
                                status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response({'message': 'No such User (therapist or client) exists'}, status=status.HTTP_404_NOT_FOUND)
