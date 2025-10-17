from django.urls import path
from .views import LoginView, RegisterViewSet, UserViewSet




urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
]