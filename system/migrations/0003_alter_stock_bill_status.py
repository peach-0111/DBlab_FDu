# Generated by Django 4.0.4 on 2022-05-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_remove_guest_bill_is_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_bill',
            name='status',
            field=models.CharField(choices=[('1', '未付款'), ('2', '已付款'), ('3', '已退货'), ('4', '已到货'), ('5', '已入库')], default='1', max_length=2, verbose_name='状态'),
        ),
    ]
