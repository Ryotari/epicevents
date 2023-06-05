from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer

User = get_user_model()

class SignupView(generics.CreateAPIView):
    """View used to create an account"""
    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.all()