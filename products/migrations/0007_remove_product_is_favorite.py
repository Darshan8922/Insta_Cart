# Generated by Django 5.0.4 on 2024-04-23 09:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="is_favorite",
        ),
    ]
