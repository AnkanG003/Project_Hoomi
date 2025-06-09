from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from property.models import Property
from property.serializers import PropertySerializer
from .models import Order
from .serializers import OrderSerializer


def order_summary_view(request):
    property_id = request.GET.get('property_id')
    property_obj = get_object_or_404(Property, id=property_id)
    return render(request, 'pages/order_summary.html', {'property': property_obj})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'tenant':
            return Order.objects.filter(tenant=user)
        elif user.user_type == 'landlord':
            return Order.objects.filter(property__landlord=user)
        return Order.objects.none()

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user)