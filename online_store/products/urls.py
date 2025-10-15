from django.urls import path

from accounts import views as accounts_views
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import get_user_model

User = get_user_model()
router = DefaultRouter()
router.register(r'users', accounts_views.UserViewSet, basename='user')
urlpatterns = router.urls
