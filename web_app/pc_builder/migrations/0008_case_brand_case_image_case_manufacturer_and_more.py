# Generated by Django 5.0.4 on 2024-04-15 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pc_builder", "0007_configuration_cpu_cooler"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pc_builder.brand",
            ),
        ),
        migrations.AddField(
            model_name="case",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/components/"
            ),
        ),
        migrations.AddField(
            model_name="case",
            name="manufacturer",
            field=models.CharField(
                choices=[("intel", "Intel"), ("amd", "AMD"), ("nvidia", "Nvidia")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="case",
            name="msrp_price",
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="case",
            name="name",
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="powersupply",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pc_builder.brand",
            ),
        ),
        migrations.AddField(
            model_name="powersupply",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/components/"
            ),
        ),
        migrations.AddField(
            model_name="powersupply",
            name="manufacturer",
            field=models.CharField(
                choices=[("intel", "Intel"), ("amd", "AMD"), ("nvidia", "Nvidia")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="powersupply",
            name="msrp_price",
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="powersupply",
            name="name",
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="storage",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pc_builder.brand",
            ),
        ),
        migrations.AddField(
            model_name="storage",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/components/"
            ),
        ),
        migrations.AddField(
            model_name="storage",
            name="manufacturer",
            field=models.CharField(
                choices=[("intel", "Intel"), ("amd", "AMD"), ("nvidia", "Nvidia")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="storage",
            name="msrp_price",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="storage",
            name="name",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
