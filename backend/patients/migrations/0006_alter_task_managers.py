# Generated by Django 5.0.1 on 2024-02-13 18:37

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0005_alter_task_active"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="task",
            managers=[
                ("list_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
