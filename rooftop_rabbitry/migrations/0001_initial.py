# Generated by Django 4.2 on 2023-05-03 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RabbitBreed",
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
                ("breed_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Rabbit",
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
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("weight", models.IntegerField()),
                ("color", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Available", "Available"),
                            ("Sold", "Sold"),
                            ("Reserved", "Reserved"),
                        ],
                        default="Available",
                        max_length=50,
                    ),
                ),
                (
                    "breed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooftop_rabbitry.rabbitbreed",
                    ),
                ),
            ],
        ),
    ]