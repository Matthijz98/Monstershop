from django.db import models
from filer.fields.image import FilerImageField


class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=128)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="childs", on_delete=models.CASCADE)

    def __str__(self):
        full_path = [self.product_category_name]
        k = self.parent
        while k is not None:
            full_path.append(k.product_category_name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class ProductBrand(models.Model):
    product_brand_name = models.CharField(max_length=128)
    product_brand_img = FilerImageField(null=True, blank=True, related_name="product_brand_img", on_delete=models.CASCADE)


class Product(models.Model):
    product_name = models.CharField(max_length=512)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    product_description = models.TextField()
    product_min_order_amount = models.FloatField(default=0)
    product_max_order_amount = models.FloatField(null=True, blank=True)
    product_created_at = models.DateTimeField()
    product_updated_at = models.DateTimeField()
    product_price = models.DecimalField(decimal_places=2, max_digits=10)


class ProductField(models.Model):
    product_field_name = models.CharField(max_length=128)


class ProductFieldDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_field = models.ForeignKey(ProductField, on_delete=models.PROTECT)
    value = models.TextField()


class ProductImg(models.Model):
    product_img_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_img_img = FilerImageField(null=True, blank=True, related_name="product_img", on_delete=models.CASCADE)
    product_img_alt_text = models.CharField(max_length=64)