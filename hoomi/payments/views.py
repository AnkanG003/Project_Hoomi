# payments/views.py
import hmac
import hashlib
import json
import uuid
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment, PaymentMethod, Transaction, Invoice
from .serializers import PaymentSerializer, PaymentMethodSerializer, TransactionSerializer, InvoiceSerializer

import hmac
import hashlib
import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Payment, Transaction


class PaymentViewSet(viewsets.ModelViewSet):
    pass
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Payment.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class PaymentMethodViewSet(viewsets.ModelViewSet):
    pass
#     queryset = PaymentMethod.objects.all()
#     serializer_class = PaymentMethodSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return PaymentMethod.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    pass
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Transaction.objects.filter(payment__user=self.request.user)


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    pass
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Invoice.objects.filter(payment__user=self.request.user)


# # @csrf_exempt
# # def razorpay_webhook(request):
# #     if request.method != 'POST':
# #         return HttpResponseBadRequest('Invalid method')

# #     received_data = request.body
# #     received_signature = request.headers.get('X-Razorpay-Signature')

# #     secret = b'q92ZjyG@i5DyNZs'

# #     generated_signature = hmac.new(
# #         key=secret,
# #         msg=received_data,
# #         digestmod=hashlib.sha256
# #     ).hexdigest()

# #     print("Generated Signature:", generated_signature)
# #     print("Received Signature:", received_signature)
# #     print("Body:", received_data)

# #     if not hmac.compare_digest(generated_signature, received_signature or ''):
# #         return JsonResponse({'error': 'Invalid signature'}, status=400)

# #     try:
# #         payload = json.loads(received_data)
# #     except json.JSONDecodeError:
# #         return JsonResponse({'error': 'Invalid JSON'}, status=400)

# #     event = payload.get('event')

# #     if event == 'payment.captured':
# #         try:
# #             entity = payload['payload']['payment']['entity']
# #             payment_reference = entity['id']

# #             payment = Payment.objects.get(payment_reference=payment_reference)
# #             payment.status = 'successful'
# #             payment.save()

# #             Transaction.objects.create(
# #                 payment=payment,
# #                 gateway_response=entity,
# #                 status='success'
# #             )
# #         except KeyError:
# #             return JsonResponse({'error': 'Missing payment entity'}, status=400)
# #         except Payment.DoesNotExist:
# #             return JsonResponse({'error': 'Payment not found'}, status=404)

# #     return JsonResponse({'status': 'success'})

# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.conf import settings
# # from .models import Order
# import razorpay

# # Initialize Razorpay client
# client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# @csrf_exempt
# def razorpay_webhook(request):
#     return JsonResponse({'status': 'error', 'message': 'Not implemented'}, status=501)


# # def payment_status(request, order_id):
# #     try:
# #         order = Order.objects.get(razorpay_order_id=order_id)
# #         return JsonResponse({'status': 'success' if order.payment_verified else 'failed'})
# #     except Order.DoesNotExist:
# #         return JsonResponse({'status': 'failed', 'message': 'Order not found'})
