# Generated by Django 5.2 on 2025-04-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expenses",
            name="id",
        ),
        migrations.AddField(
            model_name="expenses",
            name="expense_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
