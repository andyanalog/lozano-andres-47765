# Generated by Django 4.2.5 on 2023-09-29 00:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("AppLacasona", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sendsong",
            name="message",
        ),
        migrations.AddField(
            model_name="sendsong",
            name="songname",
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
