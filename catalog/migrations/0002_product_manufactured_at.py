# Generated by Django 5.0.7 on 2024-07-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                blank=True,
                help_text="Укажите дату производства продукта",
                null=True,
                verbose_name="Дата производства продукта",
            ),
        ),
    ]