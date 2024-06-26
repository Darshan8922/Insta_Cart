# Generated by Django 5.0.4 on 2024-04-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                default=None, max_length=254, null=True, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=20),
        ),
    ]
