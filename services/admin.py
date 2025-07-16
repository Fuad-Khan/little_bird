from django.contrib import admin
from .models import Category, Area, Service

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available', 'area')
    search_fields = ('title', 'description')
    filter_horizontal = ('area',)
