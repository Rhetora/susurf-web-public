# Generated by Django 3.1.1 on 2020-10-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0002_auto_20201016_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='surfboard',
            name='watertight',
            field=models.BooleanField(default=True),
        ),
    ]
