# Generated by Django 2.1 on 2020-01-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articlepost_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
