# Generated by Django 3.1.1 on 2020-10-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Misc_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDnumber', models.IntegerField()),
                ('location', models.TextField()),
                ('item_type', models.CharField(choices=[('Leash', 'Leash'), ('Indo Board', 'Indo Board'), ('Soft Roof Rack', 'Soft Roof Rack'), ('Other', 'Other')], max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('condition', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Surfboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDnumber', models.IntegerField()),
                ('location', models.TextField()),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=6)),
                ('ability', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20)),
                ('condition', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wetsuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDnumber', models.IntegerField()),
                ('location', models.TextField()),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('w-6', 'Womens 6'), ('w-8', 'Womens 8'), ('w-10', 'Womens 10'), ('w-12', 'Womens 12'), ('w-14', 'Womens 14'), ('w-16', 'Womens 16'), ('m-S', 'Mens Small'), ('m-M', 'Mens Medium'), ('m-L', 'Mens Large'), ('m-XL', 'Mens Extra Large')], max_length=6)),
                ('thickness', models.CharField(choices=[('5/4mm', '5/4mm'), ('4/3mm', '4/3mm'), ('3/2mm', '3/2mm')], max_length=10)),
                ('condition', models.TextField(blank=True)),
            ],
        ),
    ]
