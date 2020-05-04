from django.db import models
from filer.fields.image import FilerImageField
# from order_management.models import OrderDetail


class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=128)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="childs", on_delete=models.CASCADE)

    def __str__(self):
        full_path = [self.product_category_name]
        k = self.parent
        while k is not None:
            full_path.append(k.product_category_name)
            k = k.parent
        return ' - '.join(full_path[::-1])


class ProductBrand(models.Model):
    product_brand_name = models.CharField(max_length=128)
    product_brand_img = FilerImageField(null=True, blank=True, related_name="product_brand_img", on_delete=models.CASCADE)
    product_brand_created_at = models.DateTimeField(auto_created=True)
    product_brand_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=512)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    product_description = models.TextField()
    product_min_order_amount = models.FloatField(default=0)
    product_max_order_amount = models.FloatField(null=True, blank=True)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, blank=True, null=True)
    product_created_at = models.DateTimeField(auto_created=True)
    product_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class ProductField(models.Model):
    product_field_name = models.CharField(max_length=128)

    def __str__(self):
        return self.product_field_name


class ProductFieldDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_field = models.ForeignKey(ProductField, on_delete=models.PROTECT)
    value = models.TextField()

    def __str__(self):
        return self.value


class ProductImg(models.Model):
    product_img_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_img_img = FilerImageField(null=True, blank=True, related_name="product_img", on_delete=models.CASCADE)
    product_img_alt_text = models.CharField(max_length=64)

    def __str__(self):
        return self.product_img_alt_text

