# Generated by Django 4.2.5 on 2023-10-18 02:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("AppLacasona", "0007_publicaciondeimagen"),
    ]

    operations = [
        migrations.RenameField(
            model_name="publicaciondeimagen",
            old_name="mensaje",
            new_name="descripcion",
        ),
    ]
