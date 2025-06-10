# Standard Libraries
import hmac
import hashlib
import json
from uuid import uuid4

# Django and DRF
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Razorpay SDK
import razorpay

# Models
from property.models import Property
from .models import Payment, PaymentMethod, Transaction, Invoice

# Serializers
from .serializers import (
    PaymentSerializer,
    PaymentMethodSerializer,
    TransactionSerializer,
    InvoiceSerializer
)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PaymentMethod.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(payment__user=self.request.user)


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(payment__user=self.request.user)

@csrf_exempt
def razorpay_webhook(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid method')

    received_data = request.body
    received_signature = request.headers.get('X-Razorpay-Signature')

    secret = bytes(settings.WEBHOOK_SECRET, 'utf-8')

    generated_signature = hmac.new(
        key=secret,
        msg=received_data,
        digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(generated_signature, received_signature or ''):
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    try:
        payload = json.loads(received_data)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    event = payload.get('event')

    if event == 'payment.captured':
        try:
            entity = payload['payload']['payment']['entity']
            payment_reference = entity['id']

            payment = Payment.objects.get(payment_reference=payment_reference)
            payment.status = 'successful'
            payment.save()

            Transaction.objects.create(
                payment=payment,
                gateway_response=entity,
                status='success'
            )
        except KeyError:
            return JsonResponse({'error': 'Missing payment entity'}, status=400)
        except Payment.DoesNotExist:
            return JsonResponse({'error': 'Payment not found'}, status=404)

    return JsonResponse({'status': 'success'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_razorpay_order(request):
    try:
        amount = request.data.get('amount')
        property_id = request.data.get('property_id')
        user = request.user

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        razorpay_order = client.order.create({
            "amount": int(float(amount) * 100),  # amount in paise
            "currency": "INR",
            "payment_capture": 1
        })

        try:
            property_instance = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response({"error": "Invalid property ID"}, status=400)

        payment = Payment.objects.create(
            user=user,
            property=property_instance,
            amount=amount,
            payment_reference=razorpay_order['id'],
            status="created",
            payment_gateway="Razorpay"
        )

        return Response({
            "order_id": razorpay_order["id"],
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "amount": amount,
            "currency": "INR",
            "payment_db_id": payment.id
        })
    except Exception as e:
        return Response({"error": str(e)}, status=500)
