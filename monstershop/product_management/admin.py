from django.contrib import admin
from .models import Product, ProductFieldDetails, ProductField, ProductImg, ProductCategory, ProductBrand


class ProductFieldDetailsAdmin(admin.StackedInline):
    model = ProductFieldDetails


class ProductImgAdmin(admin.StackedInline):
    model = ProductImg


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_brand", "product_price", "product_category"]
    inlines = [
        ProductFieldDetailsAdmin,
        ProductImgAdmin
    ]
    search_fields = ["product_name"]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductField)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)