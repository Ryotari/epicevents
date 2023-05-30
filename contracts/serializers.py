from rest_framework import serializers
from .models import Contract

class ContractDetailSerializer(serializers.ModelSerializer):
    """Contract Serializer for the 'retrieve' action"""
    class Meta:
        model = Contract
        fields = ['id',
                'sales_contact',
                'client',
                'date_updated',
                'date_created',
                'amount',
                'payment_due'
                ]

class ContractListSerializer(serializers.ModelSerializer):
    """Contract Serializer for the 'list' action"""
    class Meta:
        model = Contract
        fields = ['id',
                'sales_contact',
                'client',
                'amount',
                'payment_due'
                ]