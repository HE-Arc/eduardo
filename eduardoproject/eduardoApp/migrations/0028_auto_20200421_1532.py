# Generated by Django 3.0.4 on 2020-04-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduardoApp', '0027_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, default='images/notIMG.png', null=True, upload_to='images/'),
        ),
    ]
