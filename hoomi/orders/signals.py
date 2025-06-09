from django.db.models.signals import post_save
from django.dispatch import receiver
from payments.models import Payment
from .models import Order

@receiver(post_save, sender=Payment)
def create_order_after_payment(sender, instance, created, **kwargs):
    if instance.status == 'successful' and not Order.objects.filter(payment=instance).exists():
        Order.objects.create(
            tenant=instance.user,
            property=instance.property,
            payment=instance,
            status='confirmed'
        )
