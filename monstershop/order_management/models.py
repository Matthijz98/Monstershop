from django.db import models
from django.contrib.auth.models import User
from product_management.models import Product

class Country(models.Model):
    country_name = models.CharField(max_length=128)

class Address(models.Model):
    address_from_user = models.ForeignKey(User, on_delete=models.PROTECT)
    address_street_name = models.CharField(max_length=256)
    address_company_name = models.CharField(max_length=128)
    address_house_nr = models.CharField(max_length=10)
    address_region = models.CharField(max_length=128)
    address_phone = models.IntegerField()
    address_zip_code = models.CharField(max_length=8)
    address_county = models.ForeignKey(Country, on_delete=models.PROTECT)


class Shipper(models.Model):
    shipper_name = models.CharField(max_length=128)
    shipper_tracking_url = models.URLField()


class Order(models.Model):
    ordered_by = models.ForeignKey(User, on_delete=models.PROTECT)
    order_date = models.DateTimeField()
    order_required_date = models.DateTimeField()
    order_completed_date = models.DateTimeField()
    shipping_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='shipping_address')
    invoice_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='invoice_address')
    schiping_with = models.ForeignKey(Shipper, on_delete=models.PROTECT)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class OrderDetail(models.Model):
    order_details_order = models.ForeignKey(Order, on_delete=models.PROTECT)
    order_details_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order_details_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_details_discount = models.DecimalField(max_digits=10, decimal_places=2)

class Shipment(models.Model):
    shipment_of_order = models.ForeignKey(Order, on_delete=models.PROTECT)
    shipment_tracking_code = models.CharField(max_length=128)
    shipment_shipper = models.ForeignKey(Shipper, on_delete=models.PROTECT)
    shipment_date = models.DateTimeField()


class ShipmentDetails(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.PROTECT)
    shipment_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    shipment_amount_included = models.FloatField()


