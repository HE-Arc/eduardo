# Generated by Django 3.0.2 on 2020-04-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0009_orderarticle_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='article'),
            preserve_default=False,
        ),
    ]
