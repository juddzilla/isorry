from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PromptSerializer, ResponseSerializer, UserSerializer
from .models import Prompt, Response, User

# Create your views here.

class PromptsView(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    queryset = Prompt.objects.all()

class ResponsesView(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()

class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()        