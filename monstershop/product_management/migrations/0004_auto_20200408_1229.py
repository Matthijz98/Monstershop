# Generated by Django 3.0.2 on 2020-04-08 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('product_management', '0003_productimg_product_img_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimg',
            name='product_img_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_max_order_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_min_order_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_out_of_stock_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productimg',
            name='product_img_img',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_img', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_brand_name', models.CharField(max_length=128)),
                ('product_brand_img', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_brand_img', to=settings.FILER_IMAGE_MODEL)),
            ],
        ),
    ]
