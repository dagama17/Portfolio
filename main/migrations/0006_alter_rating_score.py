# Generated by Django 5.0.2 on 2024-03-31 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
