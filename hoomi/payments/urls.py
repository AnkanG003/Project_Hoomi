from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PaymentViewSet, PaymentMethodViewSet,
    TransactionViewSet, InvoiceViewSet,
    # razorpay_webhook
)

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'methods', PaymentMethodViewSet, basename='methods')
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'invoices', InvoiceViewSet, basename='invoices')

urlpatterns = [
    path('', include(router.urls)),
    # path('webhook/razorpay/', razorpay_webhook, name='razorpay-webhook'),
    # path('webhook/paypal/', paypal_webhook, name='paypal-webhook'),
]
