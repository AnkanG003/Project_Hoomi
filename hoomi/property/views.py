from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.exceptions import PermissionDenied
from django.db import models
from .models import Property, PropertyImage
from .serializers import PropertySerializer, PropertyImageSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


def post_property_view(request):
    return render(request, 'pages/post_property.html')


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        if user.user_type != 'landlord':
            raise PermissionDenied("Only landlords can post properties.")
        serializer.save(landlord=user)


class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save()

# Search Function
@api_view(['GET'])
@permission_classes([])
def search_properties(request):
    query = request.GET.get('q', '')
    if query:
        properties = Property.objects.filter(
            models.Q(title__icontains=query) |
            models.Q(city__icontains=query) |
            models.Q(state__icontains=query)
        )
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    return Response([])