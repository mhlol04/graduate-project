# Generated by Django 5.0.1 on 2024-02-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0003_rename_createnewtask_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
