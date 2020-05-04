from django.db import models
from django.contrib.auth.models import User
from product_management.models import Product


class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=128)


class location(models.Model):
    loction_name = models.CharField(max_length=64)
    location_in_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    sub_loction_of = models.ForeignKey('self', null=True, blank=True, related_name="childs", on_delete=models.CASCADE)


class Producer(models.Model):
    producer_name = models.CharField(max_length=128)
    producer_email = models.EmailField()
    producer_phone = models.CharField(max_length=64)


class BuyInOrder(models.Model):
    buy_in_order_order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_in_order_producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    buy_in_order_producer_order_id = models.CharField(max_length=128, blank=True, null=True)
    buy_in_order_order_total_ammount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)


class BuyInOrderDetail(models.Model):
    buy_in_order_detail_of_order = models.ForeignKey(BuyInOrder, on_delete=models.CASCADE)
    buy_in_order_detail_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buy_in_order_detail_ammount = models.DecimalField(max_digits=10, decimal_places=2)
    buy_in_order_detail_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_in_order_detail_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    buy_in_order_detail_total = models.DecimalField(max_digits=10, decimal_places=2,blank=True)


class BuyInOrderReceivement(models.Model):
    buy_in_order_receivement_buy_in_order = models.ForeignKey(BuyInOrder, on_delete=models.CASCADE)
    buy_in_order_receivement_received_by = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_in_order_receivement_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buy_in_order_receivement_ammount = models.DecimalField(max_digits=10, decimal_places=2)
    buy_in_order_receivement_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)