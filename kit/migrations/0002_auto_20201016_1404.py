# Generated by Django 3.1.1 on 2020-10-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='misc_item',
            name='pastBorrowers',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='surfboard',
            name='pastBorrowers',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wetsuit',
            name='pastBorrowers',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='misc_item',
            name='IDnumber',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='misc_item',
            name='location',
            field=models.TextField(default='Container'),
        ),
        migrations.AlterField(
            model_name='surfboard',
            name='IDnumber',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='surfboard',
            name='location',
            field=models.TextField(default='Container'),
        ),
        migrations.AlterField(
            model_name='wetsuit',
            name='IDnumber',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='wetsuit',
            name='location',
            field=models.TextField(default='Container'),
        ),
        migrations.AlterField(
            model_name='wetsuit',
            name='size',
            field=models.CharField(choices=[('Womens 6', 'Womens 6'), ('Womens 8', 'Womens 8'), ('Womens 10', 'Womens 10'), ('Womens 12', 'Womens 12'), ('Womens 14', 'Womens 14'), ('Womens 16', 'Womens 16'), ('Mens Small', 'Mens Small'), ('Mens Medium', 'Mens Medium'), ('Mens Large', 'Mens Large'), ('Mens Extra Large', 'Mens Extra Large')], max_length=30),
        ),
    ]
