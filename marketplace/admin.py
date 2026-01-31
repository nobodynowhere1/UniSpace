from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'status', 'created_at')
    search_fields = ('title', 'description', 'author__username')
    list_filter = ('status', 'created_at')

# Register your models here.
