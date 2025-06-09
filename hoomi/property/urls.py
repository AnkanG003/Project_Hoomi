from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, PropertyImageViewSet, post_property_view, search_properties

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')
router.register(r'property-images', PropertyImageViewSet, basename='property-image')

urlpatterns = [
    path('post_property/', post_property_view, name='post_property'),
    
    path('search/', search_properties, name='search-properties'),
    path('', include(router.urls)),
]
