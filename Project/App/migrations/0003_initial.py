# Generated by Django 5.0.2 on 2024-03-01 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("App", "0002_delete_products"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account_Details",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("Emails", models.CharField(max_length=50)),
                ("Contact_no", models.IntegerField(verbose_name=12)),
                ("Address", models.TextField()),
            ],
        ),
    ]
