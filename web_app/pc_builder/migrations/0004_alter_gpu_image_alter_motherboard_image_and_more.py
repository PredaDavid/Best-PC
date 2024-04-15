# Generated by Django 5.0.4 on 2024-04-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pc_builder", "0003_rename_price_gpu_msrp_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gpu",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/components/"
            ),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/components/"
            ),
        ),
        migrations.AlterField(
            model_name="processor",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/components/"
            ),
        ),
        migrations.AlterField(
            model_name="ram",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/components/"
            ),
        ),
    ]