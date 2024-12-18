# Generated by Django 5.1 on 2024-12-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plan",
            name="discount",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="discount"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="plan",
            name="name",
            field=models.CharField(max_length=64, unique=True, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="plan",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="price"
            ),
        ),
    ]
