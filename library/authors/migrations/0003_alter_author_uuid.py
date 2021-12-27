# Generated by Django 4.0 on 2021-12-27 18:43

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0002_remove_author_id_author_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
