# Generated by Django 5.0.4 on 2024-04-18 05:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_users_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                ("username", models.CharField(blank=True, max_length=20, null=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "role",
                    models.IntegerField(
                        choices=[(1, "Vendor"), (2, "Customer")], default=2
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="Users",
        ),
    ]
