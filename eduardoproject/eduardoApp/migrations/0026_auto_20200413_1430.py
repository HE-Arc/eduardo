# Generated by Django 3.0.4 on 2020-04-13 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0025_auto_20200413_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='orderarticle',
            name='quantity',
        ),
    ]
