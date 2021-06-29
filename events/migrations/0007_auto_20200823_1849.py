# Generated by Django 3.0.6 on 2020-08-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20200823_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='event',
            name='endDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]