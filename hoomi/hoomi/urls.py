from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # This includes all routes from the users app
    path('property/', include('property.urls')),  # Replace with your actual app name
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)