from django.db.models import Q
from rest_framework.views import APIView, Response, status
from rest_framework import viewsets
from . import models
from .authentication_classes import CsrfExemptSessionAuthentication
from .permissions import *
from . import serializers


# Create your views here.
class ViewJournalView(viewsets.ViewSet):
    """
    This ViewSet takes GET request only to show client's journal to therapists.
    This only shows those therapists that are not actively mapped to the requesting client.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsTherapist]

    def list(self, request):
        """
        This method will return the list of journals that are allowed to be accessed by requesting therapist.
        """
        clients = models.User.objects.filter(is_deleted=False, type="Client").filter(
            Q(mapping_client__is_deleted=False) & Q(mapping_client__therapist=request.user) &
            Q(mapping_client__journal_access=True) & Q(mapping_client__journal_requested="Approved")
        )
        if clients:
            serialized = serializers.JournalSerializer(clients, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No active mapped client or no active access to journal."},
                            status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """
        This method will return a particular user's journal if requesting therapist has allowed access to it.
        """
        try:
            clients = models.User.objects.filter(is_deleted=False, type="Client").filter(
                Q(mapping_client__is_deleted=False) & Q(mapping_client__therapist=request.user) &
                Q(mapping_client__journal_access=True) & Q(mapping_client__journal_requested="Approved")
            ).get(pk=pk)
            serialized = serializers.JournalSerializer(clients)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "No such client is mapped or you are not allowed to access their journal"},
                            status=status.HTTP_404_NOT_FOUND)


class ClientsView(viewsets.ViewSet):
    """
    This ViewSet will allow therapists to see their clients,
    and remove clients.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsTherapist]

    def list(self, request):
        """
        This method will be handled on GET request and will show list of clients to the therapist.
        """
        clients = models.User.objects.filter(is_deleted=False, type="Client").filter(
            Q(mapping_client__is_deleted=False) & Q(mapping_client__therapist=request.user)
        )
        if clients:
            serialized = serializers.UserSerializer(clients, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No active mapped client."},
                            status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """
        This method will return a particular client if requesting therapist is mapped.
        """
        try:
            clients = models.User.objects.filter(is_deleted=False, type="Client").filter(
                Q(mapping_client__is_deleted=False) & Q(mapping_client__therapist=request.user)
            ).get(pk=pk)
            serialized = serializers.UserSerializer(clients)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "No such client is mapped."}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        This DELETE request will allow therapists to remove the mapping to existing clients.
        """
        try:
            mapping = models.Mapping.objects.get(is_deleted=False, therapist=request.user, client__pk=pk)
            mapping.is_deleted = True
            mapping.save()
            return Response({"message": "Specified client now has been removed."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "No such client is mapped."}, status=status.HTTP_404_NOT_FOUND)


class AvailableClientView(viewsets.ViewSet):
    """
    This ViewSet will allow therapists to see available clients and request them to be mapped.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsTherapist]

    def list(self, request):
        """
        This method will return a list of active clients that are not actively mapped or have pending request
        from requesting therapist.
        """
        clients = models.User.objects.filter(is_deleted=False, type="Client").exclude(
            Q(mapping_client__is_deleted=False) & Q(mapping_client__therapist=request.user)
        ).exclude(Q(request_whom__who=request.user) & Q(request_whom__status="Pending"))
        if clients:
            serialized = serializers.UserSerializer(clients, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No available clients."},
                            status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """
        This method will return a particular client if that client is available for requesting therapist.
        """
        try:
            clients = models.User.objects.filter(is_deleted=False, type="Client").exclude(
                Q(mapping_client__is_deleted=False) & Q(mapping_client__therapist=request.user)
            ).exclude(Q(request_whom__who=request.user) & Q(request_whom__status="Pending")).get(pk=pk)
            serialized = serializers.UserSerializer(clients)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "No such client is available."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        This POST method will allow therapists to request clients for mapping.
        Required Fields:
            - client_id - id of the available client
        """
        client_id = request.data.get('client_id')
        try:
            client = models.User.objects.filter(is_deleted=False, type="Client").exclude(
                Q(mapping_client__is_deleted=False) & Q(mapping_client__therapist=request.user)
            ).exclude(Q(request_whom__who=request.user) & Q(request_whom__status="Pending")).get(pk=client_id)
            serialized = serializers.MappingRequestSerializer(data={
                'who': request.user.pk,
                'whom': client_id,
            })
            if serialized.is_valid():
                serialized.save()
                return Response({
                    "message": "Your request to be mapped has been created.",
                    "client": client_id,
                    "therapist": request.user.pk
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "No such client is available for you to request."},
                            status=status.HTTP_404_NOT_FOUND)
