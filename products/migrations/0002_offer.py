# Generated by Django 4.1.7 on 2023-03-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
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
                ("code", models.CharField(max_length=7)),
                ("description", models.CharField(max_length=200)),
                ("discount", models.FloatField()),
            ],
        ),
    ]
