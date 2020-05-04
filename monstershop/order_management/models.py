from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count, Sum
from product_management.models import Product


class Countrie(models.Model):
    country_name = models.CharField(max_length=128)

    def __str__(self):
        return self.country_name


class Address(models.Model):
    address_from_user = models.ForeignKey(User, on_delete=models.PROTECT)
    address_first_name = models.CharField(max_length=256)
    address_last_name = models.CharField(max_length=256)
    address_street_name = models.CharField(max_length=256)
    address_company_name = models.CharField(max_length=128, blank=True, null=True)
    address_house_nr = models.CharField(max_length=10)
    address_region = models.CharField(max_length=128)
    address_place_name = models.CharField(max_length=128)
    address_phone = models.IntegerField(max_length=64, null=True, blank=True)
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
    order_shipping_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='shipping_address', blank=True, null=True)
    order_invoice_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='invoice_address' , blank=True, null=True)
    order_schiping_with = models.ForeignKey(Shipper, on_delete=models.PROTECT, blank=True, null=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def ammount_of_products_in_order(self):
        return OrderDetail.objects.all().filter(order_detail_order=self.id).aggregate(total=Count("order_detail_product"))["total"]

    def save(self, *args, **kwargs):
        total = 0
        for x in self.orderdetail_set.values():
            total += x['order_detail_total']
        print(total)
        self.order_total = total
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    order_detail_order = models.ForeignKey(Order, on_delete=models.PROTECT)
    order_detail_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order_detail_amount = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    order_detail_unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    order_detail_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_detail_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        if not self.order_detail_unit_price:
            self.order_detail_unit_price = Product.objects.get(id=self.order_detail_product_id).product_price
        self.order_detail_total = (self.order_detail_amount * self.order_detail_unit_price) - self.order_detail_discount
        super(OrderDetail, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


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


