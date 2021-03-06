# Generated by Django 4.0.5 on 2022-06-13 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Warehouse',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BackLog.warehouse')),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
    ]
