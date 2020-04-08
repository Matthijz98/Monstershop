from django.contrib import admin
from .models import Product, ProductFieldDetails, ProductField, ProductImg


class ProductFieldDetailsAdmin(admin.StackedInline):
    model = ProductFieldDetails


class ProductImgAdmin(admin.StackedInline):
    model = ProductImg


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductFieldDetailsAdmin,
        ProductImgAdmin
    ]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductField)