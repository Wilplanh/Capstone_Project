from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginViewSet.as_view({'get': 'list'}), name='login'),
    path('register/', views.RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('profile/', views.ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='profile'),
]