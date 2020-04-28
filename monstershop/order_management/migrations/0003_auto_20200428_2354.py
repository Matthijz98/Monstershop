# Generated by Django 3.0.2 on 2020-04-28 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0002_auto_20200428_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 21, 54, 16, 746948, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 21, 54, 16, 746948, tzinfo=utc)),
        ),
    ]
