from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, order_summary_view

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('order-summery/', order_summary_view, name='order-summery'),
    path('', include(router.urls)),
]
