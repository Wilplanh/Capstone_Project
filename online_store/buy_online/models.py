from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class cart (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Total: {self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"

class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Cart {self.cart.id}"

class payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment of {self.amount} for Order {self.order.id}"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} - Rating: {self.rating}"    

