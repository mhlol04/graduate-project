# Generated by Django 5.0.1 on 2024-02-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0004_task_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
