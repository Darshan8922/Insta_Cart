# Generated by Django 5.0.4 on 2024-04-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_user_forgot_password_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="access_token",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="refresh_token",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]