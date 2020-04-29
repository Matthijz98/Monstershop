# Generated by Django 3.0.2 on 2020-04-29 20:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0002_auto_20200429_2206'),
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
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 20, 13, 38, 319406, tzinfo=utc)),
        ),
    ]