Django E-commerce API

This project is a backend API for an E-commerce platform built with Django and Django REST Framework (DRF). It provides core features for managing products, carts, orders, payments, and reviews.

Features

Product Management: Create, update, delete, and list products with details like name, description, price, category, stock, and images.

Cart System: Add products to a cart, manage quantities, and retrieve cart items.

Orders & Checkout: Place orders with multiple items and track their total cost.

Payments: Record payments with amount, method, and timestamp.

Reviews: Allow users to rate and review products.

Models Overview
Product

Represents items available in the store.

name, description, price, category, stock_quantity, image_url

Cart & CartItem

Cart: Temporary storage of products before checkout.

CartItem: Represents individual products and their quantities within a cart.

Order & OrderItem

Order: Finalized purchase including multiple products.

OrderItem: Links products to orders with specific quantities.

Payment

Handles transactions for orders.

amount, payment_date, payment_method

Review

Allows customers to leave feedback.

rating, comment, created_at