# Generated by Django 5.2 on 2025-04-11 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="expenses",
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
                ("name", models.CharField(max_length=100)),
                (
                    "expense",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1, "Invalid value")
                        ]
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Healthcare", "Healthcare"),
                            ("Education", "Education"),
                            ("Entertainment", "Entertainment"),
                            ("Utilities", "Utilities"),
                            ("Groceries", "Groceries"),
                            ("Memberships", "Memberships"),
                            ("Debt", "Debt"),
                            ("Emergency Fund", "Emergency Fund"),
                            ("Other", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
