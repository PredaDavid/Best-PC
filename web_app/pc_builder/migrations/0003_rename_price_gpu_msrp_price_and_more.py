# Generated by Django 5.0.4 on 2024-04-14 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pc_builder", "0002_case_powersupply_storage_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="gpu",
            old_name="price",
            new_name="msrp_price",
        ),
        migrations.RenameField(
            model_name="motherboard",
            old_name="price",
            new_name="msrp_price",
        ),
        migrations.RenameField(
            model_name="processor",
            old_name="price",
            new_name="msrp_price",
        ),
        migrations.RenameField(
            model_name="ram",
            old_name="price",
            new_name="msrp_price",
        ),
    ]