# Generated by Django 3.0.6 on 2020-08-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20200823_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='endDateTime',
        ),
        migrations.AddField(
            model_name='event',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]