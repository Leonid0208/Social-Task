# Generated by Django 2.0.5 on 2020-09-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_remove_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
