# Generated by Django 5.0.4 on 2024-04-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='quantity',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
    ]