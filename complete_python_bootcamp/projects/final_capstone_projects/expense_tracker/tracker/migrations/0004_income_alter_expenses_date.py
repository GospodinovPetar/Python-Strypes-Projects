# Generated by Django 5.2 on 2025-04-14 10:32

import django.core.validators
import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0003_expenses_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
            fields=[
                ("income_id", models.AutoField(primary_key=True, serialize=False)),
                ("source", models.CharField(max_length=100)),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.01"))
                        ],
                    ),
                ),
                ("date", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name="expenses",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
