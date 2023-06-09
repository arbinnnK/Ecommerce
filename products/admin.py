from django.contrib import admin
from products.models import Category, Subcategory, Type, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption')

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'category')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'category')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image', 'discount', 'status', 'type', 'brand', 'features', 'details', 'specification')
