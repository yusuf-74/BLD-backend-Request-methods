# Generated by Django 4.1.2 on 2022-10-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("FirstName", models.CharField(max_length=20)),
                ("LastName", models.CharField(max_length=20)),
                ("age", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
