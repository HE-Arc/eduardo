# Generated by Django 3.0.4 on 2020-04-13 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0024_auto_20200413_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='availlable',
            new_name='available',
        ),
    ]