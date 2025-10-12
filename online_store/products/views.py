from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.db.models import Q

# Create your views here.



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Placeholder permission. For now, any authenticated user can create/edit products.
    You can extend this to check ownership.
    """
    def has_permission(self, request, view):
        # Allow read-only for everyone, write for authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class ProductViewSet(viewsets.ModelViewSet):
    """
    list/retrieve/create/update/destroy + supports:
    - search by name (partial)
    - filter by category (id or slug), min_price, max_price, in_stock
    - pagination from settings
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_date', 'stock_quantity']
    filterset_fields = ['category__id', 'category__slug']

    def get_queryset(self):
        qs = super().get_queryset()
        # Price range filter
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        in_stock = self.request.query_params.get('in_stock')  # 'true' means stock_quantity > 0

        if min_price:
            try:
                qs = qs.filter(price__gte=min_price)
            except ValueError:
                pass
        if max_price:
            try:
                qs = qs.filter(price__lte=max_price)
            except ValueError:
                pass
        if in_stock is not None:
            if in_stock.lower() in ['true', '1', 'yes']:
                qs = qs.filter(stock_quantity__gt=0)
            elif in_stock.lower() in ['false', '0', 'no']:
                qs = qs.filter(stock_quantity=0)
        return qs

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
