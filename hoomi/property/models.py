from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PropertyType(models.TextChoices):
    APARTMENT = "Apartment"
    HOUSE = "House"
    STUDIO = "Studio"
    PG = "PG"
    VILLA = "Villa"
    OTHER = "Other"

class FurnishingStatus(models.TextChoices):
    FURNISHED = "Furnished"
    UNFURNISHED = "Unfurnished"
    SEMI_FURNISHED = "Semi-Furnished"

class Property(models.Model):
    landlord = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=False, blank=True)  # For SEO URLs
    description = models.TextField()
    property_type = models.CharField(max_length=50, choices=PropertyType.choices, default=PropertyType.APARTMENT)
    furnishing = models.CharField(max_length=50, choices=FurnishingStatus.choices, default=FurnishingStatus.UNFURNISHED)

    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area_sqft = models.PositiveIntegerField()  # Built-up area
    available_from = models.DateField()

    # images = models.ImageField(upload_to='property_images/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.city}"

    class Meta:
        ordering = ['-created_at']

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
