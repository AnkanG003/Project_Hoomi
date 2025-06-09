from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    tenant_username = serializers.ReadOnlyField(source='tenant.username')
    property_title = serializers.ReadOnlyField(source='property.title')

    class Meta:
        model = Order
        fields = [
            'id', 'tenant', 'tenant_username', 'property', 'property_title',
            'payment', 'start_date', 'end_date', 'status',
            'special_request', 'is_active', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'status', 'is_active', 'created_at', 'updated_at']
