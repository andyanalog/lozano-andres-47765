# Generated by Django 4.2.5 on 2023-10-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppLacasona", "0004_askanything_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutMe",
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
            ],
        ),
    ]