# Generated by Django 3.0.4 on 2020-04-13 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0021_auto_20200413_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eduardoApp.State'),
        ),
    ]
