from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'property', 'status', 'start_date', 'end_date', 'created_at')
    list_filter = ('status', 'is_active', 'created_at')
    search_fields = ('tenant__username', 'property__title')
    readonly_fields = ('created_at', 'updated_at')