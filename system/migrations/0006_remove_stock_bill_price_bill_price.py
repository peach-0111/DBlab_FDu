# Generated by Django 4.0.4 on 2022-05-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_remove_bill_price_stock_bill_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_bill',
            name='price',
        ),
        migrations.AddField(
            model_name='bill',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]
