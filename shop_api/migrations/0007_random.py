# Generated by Django 4.0.4 on 2022-05-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0006_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='Random',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
    ]