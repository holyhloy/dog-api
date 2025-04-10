# Generated by Django 5.2 on 2025-04-09 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_dog_model_refactored'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='breeds',
                                    to='api.breed'),
        ),
    ]
