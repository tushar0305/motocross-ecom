from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_key', 'total_amount', 'full_name', 'address','phone','billing_status']
    list_filter = ['billing_status']


@admin.register(OrderItem)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'order', 'quantity']
    list_filter = ['quantity']
