# Generated by Django 5.0.4 on 2024-04-15 12:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pc_builder", "0004_alter_gpu_image_alter_motherboard_image_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="configuration",
            old_name="processor",
            new_name="cpu",
        ),
        migrations.RenameField(
            model_name="configuration",
            old_name="motherboard",
            new_name="mobo",
        ),
    ]
