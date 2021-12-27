# Generated by Django 4.0 on 2021-12-26 17:58

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.UUID("88d78533-a951-4838-a7d9-b774ab7a0742"), primary_key=True, serialize=False
                    ),
                ),
                ("username", models.CharField(max_length=64, unique=True)),
                ("firstname", models.CharField(max_length=64)),
                ("lastname", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
