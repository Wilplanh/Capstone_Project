from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

# Create your views here.



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
    search_fields = ['name', 'category']
    filterset_fields = {
        'category': ['exact'],
        'price': ['gte', 'lte'],
        'stock_quantity': ['gte'],
    }


    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False)
    def by_category(self, request, category=None):
        queryset = Product.objects.filter(category__iexact=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def by_name(self, request, name=None):
        queryset = Product.objects.filter(name__icontains=name)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'              # match the model field name
    lookup_url_kwarg = 'review_pk'   # match your URL


    def get_queryset(self):
        # Filter reviews by product_id from the URL
        product_id = self.kwargs.get('pk')
        return Review.objects.filter(product_id=product_id)

    def perform_create(self, serializer):
        # Get the product from the URL and save the review
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, product=product)
