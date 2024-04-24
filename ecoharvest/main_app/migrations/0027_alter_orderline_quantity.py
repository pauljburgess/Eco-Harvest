# Generated by Django 5.0.4 on 2024-04-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_alter_orderline_quantity_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='quantity',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='1', max_length=1),
        ),
    ]
