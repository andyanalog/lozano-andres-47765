# Generated by Django 4.2.5 on 2023-10-13 02:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppLacasona", "0006_avatar_delete_aboutme"),
    ]

    operations = [
        migrations.CreateModel(
            name="PublicacionDeImagen",
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
                ("imagen", models.ImageField(upload_to="imagenes/")),
                ("mensaje", models.TextField()),
            ],
        ),
    ]