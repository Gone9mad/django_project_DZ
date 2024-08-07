from django.contrib import admin
from catalog.models import Product, Category, BlogPost, Version

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'purchase_price')
    list_filter = ('category',)
    search_fields = ('name', 'descriptions',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_of_creation', 'publication')
    list_filter = ('publication',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name')
    list_filter = ('product', 'current_version_indicator')