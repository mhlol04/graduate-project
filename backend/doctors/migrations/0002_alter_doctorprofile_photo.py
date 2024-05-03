# Generated by Django 5.0.1 on 2024-03-24 21:19

import doctors.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctorprofile",
            name="photo",
            field=models.ImageField(
                default="user.png", upload_to=doctors.models.upload_photo
            ),
        ),
    ]
