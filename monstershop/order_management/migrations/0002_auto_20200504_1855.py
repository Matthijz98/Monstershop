# Generated by Django 3.0.2 on 2020-05-04 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='invoice_address',
            new_name='order_invoice_address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='schiping_with',
            new_name='order_schiping_with',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='shipping_address',
            new_name='order_shipping_address',
        ),
        migrations.AddField(
            model_name='address',
            name='address_first_name',
            field=models.CharField(default='first name', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='address_last_name',
            field=models.CharField(default='last name', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order_detail_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='address_company_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_phone',
            field=models.IntegerField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 16, 54, 12, 693391, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order_detail_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order_detail_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
