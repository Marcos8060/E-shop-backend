# Generated by Django 4.0.4 on 2022-05-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0002_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soon',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]