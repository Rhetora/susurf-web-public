# Generated by Django 3.0.6 on 2020-08-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20200827_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekendsignupentry',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]