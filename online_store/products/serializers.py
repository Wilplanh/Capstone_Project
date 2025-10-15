from rest_framework import serializers
from .models import Product, Cart, CartItem, Order, OrderItem, Payment, Review
from django.contrib.auth import get_user_model


User = get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        if data.get('price') is None or data['price'] <= 0:
            raise serializers.ValidationError({'price': 'Price must be greater than 0.'})
        if not data.get('name'):
            raise serializers.ValidationError({'name': 'Name is required.'})
        if data.get('stock_quantity') is None or data['stock_quantity'] < 0:
            raise serializers.ValidationError({'stock_quantity': 'Stock quantity must be 0 or higher.'})
        return data

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'