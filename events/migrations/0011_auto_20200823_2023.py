# Generated by Django 3.0.6 on 2020-08-23 19:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0010_auto_20200823_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='usersList',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]