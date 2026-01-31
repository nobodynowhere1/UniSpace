from django.contrib import admin

from .models import LostFoundItem


@admin.register(LostFoundItem)
class LostFoundItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'location', 'author', 'created_at')
    search_fields = ('title', 'description', 'location', 'author__username')
    list_filter = ('status', 'created_at')

# Register your models here.
