# Generated by Django 5.0.4 on 2024-04-15 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pc_builder", "0006_cpucooler"),
    ]

    operations = [
        migrations.AddField(
            model_name="configuration",
            name="cpu_cooler",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pc_builder.cpucooler",
            ),
        ),
    ]
