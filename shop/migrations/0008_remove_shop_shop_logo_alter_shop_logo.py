# Generated by Django 5.0.4 on 2024-04-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0007_shop_logo_alter_shop_shop_logo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shop",
            name="shop_logo",
        ),
        migrations.AlterField(
            model_name="shop",
            name="logo",
            field=models.CharField(),
        ),
    ]
