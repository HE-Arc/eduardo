# Generated by Django 3.0.4 on 2020-04-13 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0020_auto_20200412_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
