# Generated by Django 5.0.4 on 2024-05-01 18:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
