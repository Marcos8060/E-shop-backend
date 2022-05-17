# Generated by Django 4.0.4 on 2022-05-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0003_item_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='delivery',
            field=models.CharField(choices=[('4 days delivery', '4 DAYS DELIVERY'), ('fast delivery', 'FAST DELIVERY')], default='fastdelivery', max_length=30),
        ),
    ]