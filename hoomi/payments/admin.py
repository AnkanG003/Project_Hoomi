from django.contrib import admin
from .models import Payment, PaymentMethod, Transaction, Invoice

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'property', 'amount', 'status', 'payment_gateway', 'timestamp')
    list_filter = ('status', 'payment_gateway', 'timestamp')
    search_fields = ('user__email', 'property__title', 'payment_reference')
    readonly_fields = ('id', 'timestamp', 'updated_at')


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('user', 'method_type', 'provider', 'last4', 'upi_id', 'is_active', 'created_at')
    list_filter = ('method_type', 'is_active')
    search_fields = ('user__email', 'provider', 'upi_id')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('payment', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('payment__payment_reference',)
    readonly_fields = ('gateway_response',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'payment', 'billing_date', 'due_date', 'is_paid')
    list_filter = ('is_paid', 'billing_date')
    search_fields = ('invoice_number', 'payment__user__email')
