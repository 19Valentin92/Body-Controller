# Generated by Django 4.1.3 on 2022-12-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_healthmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="Calories",
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
                ("defg", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="HealthModel",
        ),
    ]
