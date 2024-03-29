# Generated by Django 5.0.3 on 2024-03-08 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the product category', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the product feature', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(blank=True, help_text='Upload the product image', null=True, upload_to='products/')),
                ('hide_product', models.BooleanField(default=False, help_text='Check this box to hide the product')),
                ('hide_quantity', models.BooleanField(default=False, help_text='Check this box to hide the product quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(help_text='Select the product category', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
                ('features', models.ManyToManyField(help_text='Select the product features', related_name='products', to='products.feature')),
            ],
        ),
    ]
