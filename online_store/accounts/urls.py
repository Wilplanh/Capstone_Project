from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistrationViewSet, UserViewSet



urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('register/', RegistrationViewSet.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    ]
