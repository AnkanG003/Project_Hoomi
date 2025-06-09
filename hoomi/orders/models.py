from django.db import models
from django.conf import settings
from property.models import Property
from payments.models import Payment
import uuid

class OrderStatus(models.TextChoices):
    PENDING = "Pending", "Pending"
    CONFIRMED = "Confirmed", "Confirmed"
    CANCELLED = "Cancelled", "Cancelled"
    COMPLETED = "Completed", "Completed"

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    payment = models.OneToOneField(
        Payment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='order'
    )

    start_date = models.DateField(help_text="Booking start date")
    end_date = models.DateField(help_text="Booking end date")
    
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    special_request = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} | {self.tenant.username} -> {self.property.title}"

    def duration_days(self):
        return (self.end_date - self.start_date).days
