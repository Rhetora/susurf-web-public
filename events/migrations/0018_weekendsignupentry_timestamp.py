# Generated by Django 3.0.6 on 2020-08-26 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20200825_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekendsignupentry',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 21, 40, 9, 113293)),
        ),
    ]
