# Generated by Django 5.0.4 on 2024-04-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0009_user_access_token_user_refresh_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="access_token",
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="forgot_password_token",
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="refresh_token",
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
