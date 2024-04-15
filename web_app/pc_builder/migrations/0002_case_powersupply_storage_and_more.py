# Generated by Django 5.0.4 on 2024-04-14 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pc_builder", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Case",
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
            ],
        ),
        migrations.CreateModel(
            name="PowerSupply",
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
                ("wattage", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Storage",
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
                ("capacity", models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name="processorgeneration",
            name="manufacturer",
        ),
        migrations.AlterField(
            model_name="processor",
            name="manufacturer",
            field=models.CharField(
                choices=[("intel", "Intel"), ("amd", "AMD"), ("nvidia", "Nvidia")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="processorsocket",
            name="manufacturer",
        ),
        migrations.RemoveField(
            model_name="processorgeneration",
            name="socket",
        ),
        migrations.RemoveField(
            model_name="processor",
            name="generation",
        ),
        migrations.AddField(
            model_name="motherboard",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pc_builder.brand",
            ),
        ),
        migrations.AddField(
            model_name="motherboard",
            name="manufacturer",
            field=models.CharField(
                choices=[("intel", "Intel"), ("amd", "AMD"), ("nvidia", "Nvidia")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="processor",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pc_builder.brand",
            ),
        ),
        migrations.AddField(
            model_name="processor",
            name="socket",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pc_builder.processorsocket",
            ),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/component/"
            ),
        ),
        migrations.AlterField(
            model_name="motherboard",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="processor",
            name="image",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="static/images/component/"
            ),
        ),
        migrations.AlterField(
            model_name="processor",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name="GPU",
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
                ("name", models.CharField(max_length=200)),
                (
                    "manufacturer",
                    models.CharField(
                        choices=[
                            ("intel", "Intel"),
                            ("amd", "AMD"),
                            ("nvidia", "Nvidia"),
                        ],
                        max_length=6,
                        null=True,
                    ),
                ),
                ("price", models.FloatField()),
                (
                    "image",
                    models.ImageField(
                        default="default.jpg",
                        null=True,
                        upload_to="static/images/component/",
                    ),
                ),
                ("vram", models.IntegerField()),
                ("base_clock", models.FloatField()),
                ("tdp", models.IntegerField()),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pc_builder.brand",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RAM",
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
                ("name", models.CharField(max_length=200)),
                (
                    "manufacturer",
                    models.CharField(
                        choices=[
                            ("intel", "Intel"),
                            ("amd", "AMD"),
                            ("nvidia", "Nvidia"),
                        ],
                        max_length=6,
                        null=True,
                    ),
                ),
                ("price", models.FloatField()),
                (
                    "image",
                    models.ImageField(
                        default="default.jpg",
                        null=True,
                        upload_to="static/images/component/",
                    ),
                ),
                ("capacity", models.IntegerField()),
                ("module_count", models.IntegerField()),
                ("speed", models.IntegerField()),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pc_builder.brand",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Configuration",
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
                ("name", models.CharField(max_length=300)),
                ("active_user_configuration", models.BooleanField(default=False)),
                (
                    "case",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pc_builder.case",
                    ),
                ),
                (
                    "motherboard",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pc_builder.motherboard",
                    ),
                ),
                (
                    "processor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pc_builder.processor",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "gpu",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pc_builder.gpu",
                    ),
                ),
                (
                    "psu",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pc_builder.powersupply",
                    ),
                ),
                ("ram", models.ManyToManyField(to="pc_builder.ram")),
                ("storage", models.ManyToManyField(to="pc_builder.storage")),
            ],
        ),
        migrations.DeleteModel(
            name="ComponentManufacturer",
        ),
        migrations.DeleteModel(
            name="ProcessorGeneration",
        ),
    ]
