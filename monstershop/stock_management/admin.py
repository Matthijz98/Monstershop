from django.contrib import admin
from .models import BuyInOrder, BuyInOrderDetail, BuyInOrderReceivement, Producer

# Register your models here.


class ProducerAdmin(admin.ModelAdmin):
    search_fields = ["producer_name"]

class BuyInOrderDetailAdmin(admin.TabularInline):
    model = BuyInOrderDetail
    autocomplete_fields = ["buy_in_order_detail_product"]


class BuyInOrderAdmin(admin.ModelAdmin):
    inlines = [BuyInOrderDetailAdmin]
    autocomplete_fields = ["buy_in_order_producer"]

admin.site.register(BuyInOrderReceivement)
admin.site.register(BuyInOrderDetail)
admin.site.register(BuyInOrder, BuyInOrderAdmin)
admin.site.register(Producer, ProducerAdmin)
