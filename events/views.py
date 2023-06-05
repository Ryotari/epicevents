from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from epicevents.permissions import IsManager, IsSales, IsSupport
from .serializers import EventListSerializer, EventDetailSerializer
from .models import Event

class EventViewset(ModelViewSet):
    """Define the permissions, serilizers and queryset for the Events endpoints"""
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsManager, IsSales]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsManager, IsSales, IsSupport]
        elif self.action == 'destroy':
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()