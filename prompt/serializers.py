from rest_framework import serializers
from .models import Prompt, Response, User

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ('id', 'parameters', 'user_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'created_at', 'ip_address')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('id', 'prompt_id', 'text')        