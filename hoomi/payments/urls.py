# payments/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PaymentViewSet, PaymentMethodViewSet,
    TransactionViewSet, InvoiceViewSet,
    razorpay_webhook,
    create_razorpay_order,
)

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'methods', PaymentMethodViewSet, basename='methods')
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'invoices', InvoiceViewSet, basename='invoices')

urlpatterns = [
    path('', include(router.urls)),
    path('webhook/razorpay/', razorpay_webhook, name='razorpay-webhook'),  # ✅ Add Razorpay webhook path
]
urlpatterns += [
    path('create-razorpay-order/', create_razorpay_order, name='create-razorpay-order'),
]