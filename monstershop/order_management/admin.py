from django.contrib import admin
from .models import Order, OrderDetail, Countrie, Shipper, Shipment, ShipmentDetails, Address
from totalsum.admin import TotalsumAdmin


class OrderDetailsAdmin(admin.StackedInline):
    model = OrderDetail


class OrderAdmin(TotalsumAdmin):
    list_display = ["id", "ordered_by", "order_date", "ammount_of_products_in_order", "order_total"]
    inlines = [
        OrderDetailsAdmin
    ]
    totalsum_list = ['order_total']
    unit_of_measure = '&euro;'


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
admin.site.register(OrderDetail)