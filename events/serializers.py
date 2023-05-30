from rest_framework import serializers
from .models import Event

class EventListSerializer(serializers.ModelSerializer):
    """Event Serializer for the 'list' action"""
    class Meta:
        model = Event
        fields = ['id',
                'name',
                'event_date',
                'client',
                'support_contact',
                'attendees']

class EventDetailSerializer(serializers.ModelSerializer):
    """Event Serializer for the 'retrieve' action"""
    class Meta:
        model = Event
        fields = ['id',
                'name',
                'event_date',
                'date_created',
                'date_updated',
                'client',
                'support_contact',
                'attendees',
                'event_status']