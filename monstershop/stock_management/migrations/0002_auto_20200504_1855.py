# Generated by Django 3.0.2 on 2020-05-04 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyinorder',
            old_name='buy_in_order_order_producer',
            new_name='buy_in_order_producer',
        ),
        migrations.RenameField(
            model_name='buyinorder',
            old_name='buy_in_order_order_producer_order_id',
            new_name='buy_in_order_producer_order_id',
        ),
        migrations.RenameField(
            model_name='buyinorderdetail',
            old_name='buy_in_oder_detail_ammount',
            new_name='buy_in_order_detail_ammount',
        ),
        migrations.RenameField(
            model_name='buyinorderdetail',
            old_name='buy_in_oder_detail_discount',
            new_name='buy_in_order_detail_discount',
        ),
        migrations.RenameField(
            model_name='buyinorderdetail',
            old_name='buy_in_oder_detail_product',
            new_name='buy_in_order_detail_product',
        ),
        migrations.RenameField(
            model_name='buyinorderdetail',
            old_name='buy_in_oder_detail_total',
            new_name='buy_in_order_detail_total',
        ),
        migrations.RenameField(
            model_name='buyinorderdetail',
            old_name='buy_in_oder_detail_unit_price',
            new_name='buy_in_order_detail_unit_price',
        ),
        migrations.AddField(
            model_name='buyinorderdetail',
            name='buy_in_order_detail_of_order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='stock_management.BuyInOrder'),
            preserve_default=False,
        ),
    ]
