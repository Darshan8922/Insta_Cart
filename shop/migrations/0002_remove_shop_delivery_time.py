# Generated by Django 5.0.4 on 2024-04-22 09:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shop",
            name="delivery_time",
        ),
    ]
