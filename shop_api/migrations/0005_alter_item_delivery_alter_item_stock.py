# Generated by Django 4.0.4 on 2022-05-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0004_alter_item_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='delivery',
            field=models.CharField(choices=[('4 days delivery', '4 DAYS DELIVERY'), ('fastdelivery', 'FASTDELIVERY')], default='fastdelivery', max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.CharField(choices=[('instock', 'IN STOCK'), ('outofstock', 'OUT OF STOCK')], default='instock', max_length=30),
        ),
    ]
