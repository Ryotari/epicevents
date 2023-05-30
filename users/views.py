from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer


class SignupView(generics.CreateAPIView):
    """View used to create an account"""
    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.all()