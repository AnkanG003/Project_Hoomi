# payments/models.py
from django.db import models
from django.conf import settings
from property.models import Property  # Assuming Property model is in hoomi app
import uuid

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_gateway = models.CharField(max_length=100)  # e.g., Stripe, Razorpay
    payment_reference = models.CharField(max_length=255, blank=True, null=True)  # Transaction ID from gateway
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.property} - {self.amount} - {self.status}"


class PaymentMethod(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('card', 'Card'),
        ('upi', 'UPI'),
        ('wallet', 'Wallet'),
        ('netbanking', 'Net Banking'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    method_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    provider = models.CharField(max_length=50)  # e.g., Visa, GooglePay
    last4 = models.CharField(max_length=4, blank=True, null=True)  # For card
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='transactions')
    gateway_response = models.JSONField()  # Store full response from Stripe/Razorpay
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Invoice(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='invoice')
    invoice_number = models.CharField(max_length=100, unique=True)
    billing_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
