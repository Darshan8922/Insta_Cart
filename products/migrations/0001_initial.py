# Generated by Django 5.0.4 on 2024-04-23 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("shop", "0010_alter_shop_logo_alter_shopcategory_logo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Measurement",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=20, unique=True)),
                ("logo", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=25)),
                ("price", models.CharField(max_length=5)),
                ("description", models.CharField(max_length=500)),
                ("m_qty", models.CharField(max_length=6)),
                ("is_favorite", models.BooleanField(default=False)),
                (
                    "measurement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.measurement",
                    ),
                ),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.shop"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productcategory",
                    ),
                ),
            ],
        ),
    ]
