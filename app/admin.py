from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced, Hello

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(Hello)
class HelloModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'id']
    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'order_date', 'status']