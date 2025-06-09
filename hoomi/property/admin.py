from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # Number of empty image forms displayed by default
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="60" style="object-fit:cover;" />'
        return ""
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'state', 'price_per_month', 'is_verified', 'is_active', 'created_at')
    list_filter = ('city', 'state', 'property_type', 'furnishing', 'is_verified', 'is_active')
    search_fields = ('title', 'city', 'state', 'address')
    ordering = ('-created_at',)
    inlines = [PropertyImageInline]
    fieldsets = (
        ("Basic Info", {
            'fields': ('landlord', 'title', 'slug', 'description')
        }),
        ("Property Details", {
            'fields': ('property_type', 'furnishing', 'bedrooms', 'bathrooms', 'area_sqft', 'price_per_month', 'available_from')
        }),
        ("Location", {
            'fields': ('address', 'city', 'state', 'pincode', 'latitude', 'longitude')
        }),
        ("Status", {
            'fields': ('is_verified', 'is_active')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image_preview')
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="60" style="object-fit:cover;" />'
        return ""
    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'
