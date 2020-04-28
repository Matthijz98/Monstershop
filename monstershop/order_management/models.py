from django.db import models
from django.contrib.auth.models import User
from product_management.models import Product
from django.utils import timezone

class Countrie(models.Model):
    country_name = models.CharField(max_length=128)

    def __str__(self):
        return self.country_name


class Address(models.Model):
    address_from_user = models.ForeignKey(User, on_delete=models.PROTECT)
    address_street_name = models.CharField(max_length=256)
    address_company_name = models.CharField(max_length=128)
    address_house_nr = models.CharField(max_length=10)
    address_region = models.CharField(max_length=128)
    address_place_name = models.CharField(max_length=128)
    address_phone = models.IntegerField()
    address_zip_code = models.CharField(max_length=8)
    address_county = models.ForeignKey(Countrie, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.address_street_name + self.address_place_name)


class Shipper(models.Model):
    shipper_name = models.CharField(max_length=128)
    shipper_tracking_url = models.URLField()

    def __str__(self):
        self.shipper_name


class Order(models.Model):
    ordered_by = models.ForeignKey(User, on_delete=models.PROTECT)
    order_date = models.DateTimeField(default=timezone.now())
    order_required_date = models.DateField(default=timezone.now, blank=True, null=True)
    order_completed_date = models.DateTimeField(blank=True, null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='shipping_address', blank=True, null=True)
    invoice_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='invoice_address' , blank=True, null=True)
    schiping_with = models.ForeignKey(Shipper, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    order_details_order = models.ForeignKey(Order, on_delete=models.PROTECT)
    order_details_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order_details_amount = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    order_details_discount = models.DecimalField(max_digits=10, decimal_places=2)


class Shipment(models.Model):
    shipment_of_order = models.ForeignKey(Order, on_delete=models.PROTECT)
    shipment_tracking_code = models.CharField(max_length=128)
    shipment_shipper = models.ForeignKey(Shipper, on_delete=models.PROTECT)
    shipment_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class ShipmentDetails(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.PROTECT)
    shipment_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    shipment_amount_included = models.FloatField()


