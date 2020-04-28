from django.contrib import admin
from .models import Order, OrderDetail, Countrie, Shipper, Shipment, ShipmentDetails, Address


class OrderDetailsAdmin(admin.StackedInline):
    model = OrderDetail


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDetailsAdmin
    ]


class ShipmentDetailsAdmin(admin.StackedInline):
    model = ShipmentDetails


class ShipmentAdmin(admin.ModelAdmin):
    inlines = [
        ShipmentDetailsAdmin
    ]

########################
# All the admin models #
########################
admin.site.register(Order, OrderAdmin)
admin.site.register(Countrie)
admin.site.register(Shipper)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Address)