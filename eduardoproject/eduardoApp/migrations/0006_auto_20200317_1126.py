# Generated by Django 3.0.3 on 2020-03-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0005_auto_20200317_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(null=True, upload_to='eduardoApp/media/photos/'),
        ),
    ]
