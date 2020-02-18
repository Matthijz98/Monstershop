from django.contrib import admin
from .models import Order, OrderDetail

class OrderDetailsAdmin(admin.StackedInline):
    model = OrderDetail

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDetailsAdmin
    ]

admin.site.register(Order, OrderAdmin)
# Register your models here.
