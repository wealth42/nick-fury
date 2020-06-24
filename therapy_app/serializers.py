from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """
    This serializer will be used to serialize the data of the User model.
    """

    class Meta:
        model = models.User
        fields = ('id', 'email')


class MappingSerializer(serializers.ModelSerializer):
    """
    This serializer will be used to serialize the data of the Mapping model.
    """
    client_email = serializers.EmailField(source='client.email', required=False)
    therapist_email = serializers.EmailField(source='therapist.email', required=False)

    class Meta:
        model = models.Mapping
        fields = ('id', 'client', 'client_email', 'therapist', 'therapist_email', 'journal_access', 'journal_requested')


class ChatSerializer(serializers.ModelSerializer):
    """
    This serializer will be used to serialize the data of the Chat model.
    """
    time = serializers.DateTimeField(source='created_at', required=False)

    class Meta:
        model = models.Chat
        fields = ('id', 'from_user', 'to_user', 'time', 'message')


class EmotionSerializer(serializers.ModelSerializer):
    """
    This serializer will be used to serialize the data of the Emotion model.
    """
    client_email = serializers.EmailField(source='client.email', required=False)
    time = serializers.DateTimeField(source='created_at', required=False)

    class Meta:
        model = models.Emotion
        fields = ('id', 'client', 'client_email', 'emotion', 'intensity', 'time')
