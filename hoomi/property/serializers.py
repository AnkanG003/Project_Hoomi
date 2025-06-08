from rest_framework import serializers
from .models import Property, PropertyImage


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'property', 'image']


class PropertySerializer(serializers.ModelSerializer):
    landlord = serializers.ReadOnlyField(source='landlord.id')  # Set automatically from request
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'landlord', 'title', 'slug', 'description',
            'property_type', 'furnishing', 'address', 'city', 'state',
            'pincode', 'latitude', 'longitude', 'price_per_month',
            'bedrooms', 'bathrooms', 'area_sqft', 'available_from',
            'images', 'is_verified', 'is_active', 'created_at', 'updated_at',
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']
