# Generated by Django 3.0.2 on 2020-04-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0010_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderarticle',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
