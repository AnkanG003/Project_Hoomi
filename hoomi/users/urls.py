from django.urls import path
from .views import index, UserListView, UserCreateView, UserDetailView, login, register
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),  # Optional homepage
    path('login', login, name="login"),
    path('register', register, name="register"),

    path('api/token/', obtain_auth_token, name='api-token'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/create/', UserCreateView.as_view(), name='user-create'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail-update'),
]
