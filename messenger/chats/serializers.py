from .models import Message, Chat
from blogs.models import User
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content', 'write_time', 'user']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nick']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()
