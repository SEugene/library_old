# Generated by Django 4.0 on 2021-12-27 18:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('897be9c2-240f-4007-88b6-988cef385f64'), primary_key=True, serialize=False),
        ),
    ]