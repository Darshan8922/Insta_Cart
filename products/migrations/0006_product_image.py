# Generated by Django 5.0.4 on 2024-04-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_alter_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]