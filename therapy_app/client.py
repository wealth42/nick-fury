from django.db.models import Q
from rest_framework.views import APIView, Response, status
from . import models
from .authentication_classes import CsrfExemptSessionAuthentication
from .permissions import *
from . import serializers


# Create your views here.
class SearchTherapistView(APIView):
    """
    This APIView takes GET request only to show available therapists to clients.
    This only shows those therapists that are not actively mapped to the requesting client.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsClient]

    def get(self, request, format=None):
        """
        This method will return the list of therapists that are not actively mapped to the requesting client.
        """
        therapists = models.User.objects.filter(is_deleted=False, type='Therapist').exclude(
            Q(mapping_therapist__client=request.user) & Q(mapping_therapist__is_deleted=False))
        serialized = serializers.UserSerializer(therapists, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class MapTherapistView(APIView):
    """
    This APIView takes GET request only to map available therapists to clients.
    This only maps those therapists that are not actively mapped to the requesting client.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsClient]

    def get(self, request, id1, format=None):
        """
        This method will map a therapist that is not actively mapped to the requesting client.
        """
        if models.User.objects.filter(is_deleted=False, type='Therapist', pk=id1).exists():
            try:
                therapist = models.User.objects.filter(is_deleted=False, type='Therapist').exclude(
                        Q(mapping_therapist__client=request.user) & Q(mapping_therapist__is_deleted=False)).get(pk=id1)
                new_mapping = models.Mapping.objects.create(client=request.user,
                                                            therapist=therapist)
                return Response({'message': 'Mapping has been created',
                                 'therapist_id': therapist.pk,
                                 'client_id': request.user.pk}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': 'The Therapist is already mapped.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No such therapist exists'}, status=status.HTTP_404_NOT_FOUND)


class MappedTherapistsView(APIView):
    """
    This APIView takes GET request only to list mapped therapists to clients.
    This only shows those therapists that are actively mapped to the requesting client.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsClient]

    def get(self, request, format=None):
        """
        This method will show therapists that are actively mapped to the requesting client.
        """
        mappings = models.Mapping.objects.filter(is_deleted=False, client=request.user)
        if mappings:
            serialized = serializers.MappingSerializer(mappings, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'There currently does not exists any active mapped therapists.'},
                            status=status.HTTP_200_OK)


class TherapistsWithJournalAccessView(APIView):
    """
    This APIView takes GET request only to list mapped therapists having journal access to clients.
    This only shows those therapists that are actively mapped and has journal access to the requesting client.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [IsClient]

    def get(self, request, format=None):
        """
        This method will show therapists that are actively mapped and has journal access to the requesting client.
        """
        mappings = models.Mapping.objects.filter(is_deleted=False, client=request.user, journal_access=True,
                                                 journal_requested="Approved")
        if mappings:
            serialized = serializers.MappingSerializer(mappings, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'There currently does not exists any active mapped therapists who has access to your '
                           'journal. '
            }, status=status.HTTP_200_OK)
