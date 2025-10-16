from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

# Create your views here.

user = get_user_model()

    # Pagination for product listings
class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



    # CRUD for products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'category__name']
    filterset_fields = {
        'category__name': ['exact'],
        'price': ['gte', 'lte'],
        'stock_quantity': ['gte'],
    }


    def perform_create(self, serializer):
        serializer.save()




