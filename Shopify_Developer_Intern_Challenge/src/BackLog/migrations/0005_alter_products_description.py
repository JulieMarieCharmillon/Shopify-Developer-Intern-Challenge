# Generated by Django 4.0.5 on 2022-06-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackLog', '0004_alter_products_options_alter_warehouse_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
