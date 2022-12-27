# Generated by Django 4.1.3 on 2022-12-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_diet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diet",
            name="activity",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="diet",
            name="age",
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="diet",
            name="gender",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="diet",
            name="height",
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="diet",
            name="users",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="diet",
            name="weight",
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
